import os
from datetime import timedelta

from flask import Flask, jsonify, redirect, render_template, request, session, url_for
from flask_session import Session
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
from graph_excel import (
    TokenExpiredError,
    create_employee,
    find_employee,
    get_table_rows,
    update_employee,
)

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# Server-side filesystem session — keeps MSAL cache off the cookie and
# removes the 4 KB cookie-size limit that would drop the refresh token.
_SESSION_DIR = os.path.join(os.path.dirname(__file__), ".flask_session")
os.makedirs(_SESSION_DIR, exist_ok=True)

app.config.update(
    SESSION_TYPE="filesystem",
    SESSION_FILE_DIR=_SESSION_DIR,
    SESSION_FILE_THRESHOLD=500,          # max session files before cleanup
    PERMANENT_SESSION_LIFETIME=timedelta(days=30),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",      # required for OAuth redirect flow
)
Session(app)


# ---------------------------------------------------------------------------
# MSAL token cache helpers
# ---------------------------------------------------------------------------

def _load_cache() -> msal.SerializableTokenCache:
    """Deserialize the MSAL token cache stored in the server-side session."""
    cache = msal.SerializableTokenCache()
    serialized = session.get("msal_token_cache")
    if serialized:
        cache.deserialize(serialized)
    return cache


def _save_cache(cache: msal.SerializableTokenCache) -> None:
    """Persist the MSAL cache back to the session if it changed."""
    if cache.has_state_changed:
        session["msal_token_cache"] = cache.serialize()


def _build_msal_app(cache: msal.SerializableTokenCache) -> msal.ConfidentialClientApplication:
    return msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=AUTHORITY,
        client_credential=CLIENT_SECRET,
        token_cache=cache,
    )


def get_valid_token(force_refresh: bool = False) -> str | None:
    """
    Return a valid access token using MSAL's silent flow.

    - If the cached access token is still valid, returns it immediately.
    - If it is expired, MSAL automatically uses the refresh token to get
      a new one (no user interaction needed).
    - force_refresh=True bypasses the cache and always calls Azure AD
      using the refresh token — used after an unexpected 401 from Graph.
    - Returns None when there is no account in the cache (user must log in).
    """
    cache = _load_cache()
    msal_app = _build_msal_app(cache)

    accounts = msal_app.get_accounts()
    if not accounts:
        return None

    result = msal_app.acquire_token_silent(
        SCOPES,
        account=accounts[0],
        force_refresh=force_refresh,
    )
    _save_cache(cache)

    if result and "access_token" in result:
        return result["access_token"]

    # Refresh token is missing or also expired — user must log in again.
    return None


# ---------------------------------------------------------------------------
# Graph call wrapper with automatic 401 retry
# ---------------------------------------------------------------------------

class AuthError(Exception):
    """Raised when a valid token cannot be obtained."""
    pass


def call_graph(graph_func, *args, **kwargs):
    """
    Execute graph_func(token, *args, **kwargs) with one automatic retry
    on TokenExpiredError.

    MSAL's acquire_token_silent() normally prevents 401s by refreshing
    the access token before it expires.  The retry with force_refresh=True
    handles the rare edge cases: clock skew between server and Azure AD,
    or a token that was revoked server-side mid-session.
    """
    token = get_valid_token()
    if not token:
        raise AuthError("Not authenticated")

    try:
        return graph_func(token, *args, **kwargs)

    except TokenExpiredError:
        # Graph rejected the token — force a hard refresh via the refresh token.
        token = get_valid_token(force_refresh=True)
        if not token:
            raise AuthError("Session expired. Please log in again.")
        return graph_func(token, *args, **kwargs)


# ---------------------------------------------------------------------------
# Auth helpers
# ---------------------------------------------------------------------------

def require_token():
    """Return (token, None) or (None, error_response)."""
    token = get_valid_token()
    if not token:
        return None, (jsonify({"error": "Not authenticated", "login_required": True}), 401)
    return token, None


def get_department_or_404(department_key):
    dep = DEPARTMENTS.get(str(department_key or "").upper())
    if not dep:
        return None, (jsonify({"error": "Invalid department"}), 404)
    return dep, None


def _auth_error_response(exc: AuthError):
    return jsonify({"error": str(exc), "login_required": True}), 401


# ---------------------------------------------------------------------------
# Routes — Auth
# ---------------------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    # Make the session permanent so the cookie survives browser restarts.
    session.permanent = True
    auth_url = _build_msal_app(_load_cache()).get_authorization_request_url(
        SCOPES,
        redirect_uri=REDIRECT_URI,
        prompt="select_account",
    )
    return redirect(auth_url)


@app.route("/auth/callback")
def auth_callback():
    # ── Step 1: check for Azure AD error in the redirect ──────────────────
    error = request.args.get("error")
    if error:
        desc = request.args.get("error_description", "No description provided")
        print(f"[AUTH] Azure AD returned error: {error} | {desc}")
        return (
            f"<h2>Authentication Error</h2>"
            f"<p><b>{error}</b></p><p>{desc}</p>"
            f"<a href='/login'>Try again</a>"
        ), 400

    code = request.args.get("code")
    if not code:
        print(f"[AUTH] Callback hit with no code. Query args: {dict(request.args)}")
        return "<h2>Missing authorization code</h2><a href='/login'>Try again</a>", 400

    # ── Step 2: exchange auth-code for tokens ──────────────────────────────
    print(f"[AUTH] Code received. Exchanging for token (redirect_uri={REDIRECT_URI})...")
    try:
        cache    = _load_cache()
        msal_app = _build_msal_app(cache)
        result   = msal_app.acquire_token_by_authorization_code(
            code,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URI,
        )
    except Exception as exc:
        import traceback; traceback.print_exc()
        return f"<h2>Token Exchange Exception</h2><p>{exc}</p><a href='/login'>Try again</a>", 500

    if "access_token" not in result:
        err  = result.get("error", "unknown_error")
        desc = result.get("error_description", str(result))
        print(f"[AUTH] Token exchange failed: {err} | {desc}")
        return (
            f"<h2>Token Error</h2>"
            f"<p><b>{err}</b></p><p>{desc}</p>"
            f"<a href='/login'>Try again</a>"
        ), 400

    # ── Step 3: persist cache + session ────────────────────────────────────
    _save_cache(cache)

    # id_token_claims can be None/{} — guarantee session["user"] is always truthy.
    claims = result.get("id_token_claims") or {}
    session["user"] = {
        "name":  claims.get("name") or claims.get("preferred_username") or "User",
        "email": claims.get("preferred_username") or claims.get("upn") or "",
        "oid":   claims.get("oid") or claims.get("sub") or "unknown",
        **claims,
    }
    session.permanent = True        # 30-day persistent cookie

    user_name = session["user"].get("name", "?")
    print(f"[AUTH] Login successful. User: {user_name}. Redirecting to index.")
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


# ---------------------------------------------------------------------------
# Routes — API
# ---------------------------------------------------------------------------

@app.route("/api/me")
def api_me():
    # Primary auth check: does the MSAL cache contain a valid account?
    # More reliable than checking session["user"] which can be falsy if
    # Azure AD returns empty id_token_claims.
    print(f"[API/ME] Session keys present: {list(session.keys())}")
    token = get_valid_token()
    user  = session.get("user")
    authenticated = bool(token) or bool(user)
    print(f"[API/ME] authenticated={authenticated}  has_token={bool(token)}  has_user={bool(user)}")
    return jsonify({"authenticated": authenticated, "user": user})


@app.route("/api/departments")
def api_departments():
    return jsonify([
        {"key": key, "label": dep["label"], "workbook_name": dep["workbook_name"]}
        for key, dep in DEPARTMENTS.items()
    ])


@app.route("/api/<department_key>/employees")
def api_list_employees(department_key):
    _, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error

    holidays = request.args.getlist("holiday")
    try:
        _, employees = call_graph(get_table_rows, department)
        enriched = []
        for employee in employees:
            calc = calculate_status(employee, holidays)
            public_employee = {k: v for k, v in employee.items() if not k.startswith("_")}
            public_employee["calculated"] = calc
            enriched.append(public_employee)
        return jsonify({"employees": enriched})
    except AuthError as exc:
        return _auth_error_response(exc)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees/<employee_id>")
def api_get_employee(department_key, employee_id):
    _, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error

    holidays = request.args.getlist("holiday")
    try:
        employee = call_graph(find_employee, department, employee_id)
        if not employee:
            return jsonify({"error": "Employee not found"}), 404
        employee = {k: v for k, v in employee.items() if not k.startswith("_")}
        employee["calculated"] = calculate_status(employee, holidays)
        return jsonify(employee)
    except AuthError as exc:
        return _auth_error_response(exc)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees", methods=["POST"])
def api_create_employee(department_key):
    _, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error

    payload = request.json or {}
    try:
        record = {
            "Employee ID":    payload.get("Employee ID", ""),
            "Employee Name":  payload.get("Employee Name", ""),
            "CSA Start Date": payload.get("CSA Start Date", ""),
        }
        created = call_graph(create_employee, department, record)
        return jsonify({"message": "Created", "employee": created})
    except AuthError as exc:
        return _auth_error_response(exc)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


@app.route("/api/<department_key>/employees/<employee_id>", methods=["PATCH"])
def api_update_employee(department_key, employee_id):
    _, error = require_token()
    if error:
        return error
    department, error = get_department_or_404(department_key)
    if error:
        return error

    payload = request.json or {}
    holidays = payload.pop("_holidays", [])
    try:
        calc = calculate_status(payload, holidays)
        payload["Due date"]                     = calc["due_date"]
        payload["Remaining days (working days)"] = calc["remaining_days"] if calc["remaining_days"] is not None else ""
        payload["On time"]                      = calc["on_time"]
        payload["Actual Status"]                = calc["status"]
        payload["Total Training Days"]          = calc["allowed_days"] if calc["allowed_days"] is not None else ""
        updated = call_graph(update_employee, department, employee_id, payload)
        updated["calculated"] = calc
        return jsonify({"message": "Updated", "employee": updated})
    except AuthError as exc:
        return _auth_error_response(exc)
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    # use_reloader=False prevents the Werkzeug reloader from spawning a second
    # process that can cause session-file conflicts on Windows.
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
