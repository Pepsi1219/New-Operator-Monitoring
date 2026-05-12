from flask import Flask, jsonify, redirect, render_template, request, session, url_for
import msal

from config import (
    AUTHORITY,
    CLIENT_ID,
    CLIENT_SECRET,
    DEPARTMENTS,
    FLASK_SECRET_KEY,
    REDIRECT_URI,
    SCOPES,
)
from business_rules import calculate_status
from graph_excel import create_employee, find_employee, get_table_rows, update_employee

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


def build_msal_app(cache=None):
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
        token_cache=cache,
    )


def get_token_from_session():
    token = session.get("access_token")
    if not token:
        return None
    return token


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    auth_url = build_msal_app().get_authorization_request_url(
        SCOPES,
        redirect_uri=REDIRECT_URI,
        prompt="select_account",
    )
    return redirect(auth_url)


@app.route("/auth/callback")
def auth_callback():
    code = request.args.get("code")
    if not code:
        return "Missing authorization code", 400
    result = build_msal_app().acquire_token_by_authorization_code(
        code,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
    )
    if "access_token" not in result:
        return jsonify(result), 400
    session["access_token"] = result["access_token"]
    session["user"] = result.get("id_token_claims", {})
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route("/api/me")
def api_me():
    user = session.get("user")
    return jsonify({"authenticated": bool(user), "user": user})


@app.route("/api/departments")
def api_departments():
    return jsonify([
        {"key": key, "label": dep["label"], "workbook_name": dep["workbook_name"]}
        for key, dep in DEPARTMENTS.items()
    ])


def require_token():
    token = get_token_from_session()
    if not token:
        return None, (jsonify({"error": "Not authenticated"}), 401)
    return token, None


def get_department_or_404(department_key):
    dep = DEPARTMENTS.get(str(department_key or "").upper())
    if not dep:
        return None, (jsonify({"error": "Invalid department"}), 404)
    return dep, None


@app.route("/api/<department_key>/employees")
def api_list_employees(department_key):
    token, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error

    holidays = request.args.getlist("holiday")
    try:
        _, employees = get_table_rows(token, department)
        enriched = []
        for employee in employees:
            calc = calculate_status(employee, holidays)
            public_employee = {k: v for k, v in employee.items() if not k.startswith("_")}
            public_employee["calculated"] = calc
            enriched.append(public_employee)
        return jsonify({"employees": enriched})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees/<employee_id>")
def api_get_employee(department_key, employee_id):
    token, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error
    holidays = request.args.getlist("holiday")
    try:
        employee = find_employee(token, department, employee_id)
        if not employee:
            return jsonify({"error": "Employee not found"}), 404
        employee = {k: v for k, v in employee.items() if not k.startswith("_")}
        employee["calculated"] = calculate_status(employee, holidays)
        return jsonify(employee)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees", methods=["POST"])
def api_create_employee(department_key):
    token, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error
    payload = request.json or {}
    try:
        record = {
            "Employee ID": payload.get("Employee ID", ""),
            "Employee Name": payload.get("Employee Name", ""),
            "Grade": payload.get("Grade", ""),
        }
        created = create_employee(token, department, record)
        return jsonify({"message": "Created", "employee": created})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees/<employee_id>", methods=["PATCH"])
def api_update_employee(department_key, employee_id):
    token, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error
    payload = request.json or {}
    holidays = payload.pop("_holidays", [])
    try:
        calc = calculate_status(payload, holidays)
        payload["Due date"] = calc["due_date"]
        payload["Remaining days (working days)"] = calc["remaining_days"] if calc["remaining_days"] is not None else ""
        payload["On time"] = calc["on_time"]
        payload["Actual Status"] = calc["status"]
        payload["Total Training Days"] = calc["allowed_days"] if calc["allowed_days"] is not None else ""
        updated = update_employee(token, department, employee_id, payload)
        updated["calculated"] = calc
        return jsonify({"message": "Updated", "employee": updated})
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
