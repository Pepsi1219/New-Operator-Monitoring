import base64
import urllib.parse
from contextlib import contextmanager

import requests
from config import EXCEL_COLUMNS, EXCEL_TABLE_NAME, ONEDRIVE_FOLDER

GRAPH_ROOT = "https://graph.microsoft.com/v1.0"


class GraphExcelError(Exception):
    pass


class TokenExpiredError(GraphExcelError):
    """Raised when Graph API returns 401 — access token is expired or invalid."""
    pass


def _headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }


def graph_request(token, method, path, **kwargs):
    url = f"{GRAPH_ROOT}{path}"

    default_headers = _headers(token)
    extra_headers = kwargs.pop("headers", {})
    merged_headers = {**default_headers, **extra_headers}

    response = requests.request(
        method,
        url,
        headers=merged_headers,
        timeout=60,
        **kwargs
    )

    if response.status_code == 401:
        raise TokenExpiredError(
            "Graph API returned 401 — access token expired or invalid."
        )

    if not response.ok:
        raise GraphExcelError(f"Graph API error {response.status_code}: {response.text}")

    if response.status_code == 204:
        return None

    return response.json()


def encode_sharing_url(share_url):
    encoded = base64.b64encode(share_url.encode("utf-8")).decode("utf-8")
    encoded = encoded.rstrip("=").replace("/", "_").replace("+", "-")
    return "u!" + encoded


def get_drive_item(token, department):
    """
    Locate the workbook. Access priority:
    1. Sharing URL  — always points to the exact file configured in DEPARTMENTS
    2. Direct path  — fallback (unreliable when multiple files share the same name)
    3. Drive search — last resort
    """
    workbook_name = department["workbook_name"]
    share_url     = department["share_url"]

    # ── 1. Sharing URL (most precise — unique per file) ───────────────────────
    try:
        share_id = encode_sharing_url(share_url)
        item = graph_request(
            token,
            "GET",
            f"/shares/{share_id}/driveItem",
            headers={"Prefer": "redeemSharingLinkIfNecessary"},
        )
        print(f"[DRIVE] ✓ sharing URL: {workbook_name}", flush=True)
        return item
    except GraphExcelError as e:
        print(f"[DRIVE] sharing URL failed: {e}", flush=True)

    # ── 2. Direct path-based access ──────────────────────────────────────────
    try:
        file_path    = f"{ONEDRIVE_FOLDER}/{workbook_name}"
        encoded_path = urllib.parse.quote(file_path, safe="/")
        item = graph_request(token, "GET", f"/me/drive/root:/{encoded_path}:")
        print(f"[DRIVE] ✓ path: {workbook_name}", flush=True)
        return item
    except GraphExcelError as e:
        print(f"[DRIVE] path failed: {e}", flush=True)

    # ── 3. Search in user's own drive ─────────────────────────────────────────
    q    = urllib.parse.quote(workbook_name, safe="")
    data = graph_request(token, "GET", f"/me/drive/root/search(q='{q}')")
    for item in (data.get("value") or []):
        if item.get("name") == workbook_name and "file" in item:
            print(f"[DRIVE] ✓ search: {workbook_name}", flush=True)
            return item
    raise GraphExcelError(f"Cannot locate workbook: {workbook_name}")


# ── Workbook session context manager ─────────────────────────────────────────

@contextmanager
def _workbook_session(token, drive_id, item_id):
    """
    Create a persistent workbook session for write operations.
    Sessions give proper write access and avoid the 'cannot perform operation' 403.
    Falls back to no-session mode if createSession itself fails.
    """
    session_id = None
    url_base   = f"/drives/{drive_id}/items/{item_id}/workbook"
    try:
        resp       = graph_request(token, "POST", f"{url_base}/createSession",
                                   json={"persistChanges": True})
        session_id = resp.get("id", "")
        print(f"[SESSION] created {session_id[:20]}…", flush=True)
    except GraphExcelError as exc:
        print(f"[SESSION] createSession failed ({exc}) — writing without session", flush=True)

    try:
        yield {"workbook-session-id": session_id} if session_id else {}
    finally:
        if session_id:
            try:
                graph_request(token, "POST", f"{url_base}/closeSession",
                              headers={"workbook-session-id": session_id})
                print("[SESSION] closed", flush=True)
            except GraphExcelError:
                pass


# ── Row helpers ───────────────────────────────────────────────────────────────

def row_to_object(values):
    values = values or []
    return {col: values[i] if i < len(values) else ""
            for i, col in enumerate(EXCEL_COLUMNS)}


def object_to_row(record):
    return [record.get(col, "") for col in EXCEL_COLUMNS]


# ── Table read ────────────────────────────────────────────────────────────────

def get_table_rows(token, department):
    item     = get_drive_item(token, department)
    drive_id = item["parentReference"]["driveId"]
    item_id  = item["id"]
    data     = graph_request(token, "GET",
                             f"/drives/{drive_id}/items/{item_id}"
                             f"/workbook/tables/{EXCEL_TABLE_NAME}/rows")
    rows      = data.get("value", [])
    employees = []
    for index, row in enumerate(rows):
        values = (row.get("values") or [[]])[0]
        obj    = row_to_object(values)
        emp_id = str(obj.get("Employee ID", "")).strip()
        if emp_id and emp_id != "0":
            obj["_row_index"] = index
            employees.append(obj)
    return item, employees


def find_employee(token, department, employee_id):
    _, employees = get_table_rows(token, department)
    employee_id  = str(employee_id or "").strip()
    for emp in employees:
        if str(emp.get("Employee ID", "")).strip() == employee_id:
            return emp
    return None


# ── Write via Workbook API (with session) ─────────────────────────────────────

def _write_row_add(token, drive_id, item_id, row_values):
    """Add a new row to the table — uses a workbook session for proper write access."""
    with _workbook_session(token, drive_id, item_id) as sess_hdrs:
        body = {"index": None, "values": [row_values]}
        graph_request(
            token, "POST",
            f"/drives/{drive_id}/items/{item_id}"
            f"/workbook/tables/{EXCEL_TABLE_NAME}/rows/add",
            json=body,
            headers=sess_hdrs,
        )


def _write_row_patch(token, drive_id, item_id, row_index, row_values):
    """Update an existing table row range — uses a workbook session."""
    with _workbook_session(token, drive_id, item_id) as sess_hdrs:
        body = {"values": [row_values]}
        graph_request(
            token, "PATCH",
            f"/drives/{drive_id}/items/{item_id}"
            f"/workbook/tables/{EXCEL_TABLE_NAME}"
            f"/rows/itemAt(index={row_index})/range",
            json=body,
            headers=sess_hdrs,
        )


# ── Public CRUD ───────────────────────────────────────────────────────────────

def create_employee(token, department, record):
    item, employees = get_table_rows(token, department)
    employee_id     = str(record.get("Employee ID", "")).strip()
    if not employee_id:
        raise GraphExcelError("Employee ID is required")
    if any(str(e.get("Employee ID", "")).strip() == employee_id for e in employees):
        raise GraphExcelError(f"Employee ID {employee_id} already exists")

    current_ids = []
    for emp in employees:
        try:
            current_ids.append(int(float(emp.get("ID", 0))))
        except (ValueError, TypeError):
            pass
    next_id = max(current_ids or [0]) + 1

    new_record                  = {col: "" for col in EXCEL_COLUMNS}
    new_record.update(record)
    new_record["ID"]            = next_id
    new_record["Actual Status"] = "Under basic"

    drive_id = item["parentReference"]["driveId"]
    item_id  = item["id"]
    _write_row_add(token, drive_id, item_id, object_to_row(new_record))
    return new_record


def update_employee(token, department, employee_id, patch_record):
    item, employees = get_table_rows(token, department)
    employee = None
    for emp in employees:
        if str(emp.get("Employee ID", "")).strip() == str(employee_id).strip():
            employee = emp
            break
    if not employee:
        raise GraphExcelError("Employee not found")

    merged = {col: employee.get(col, "") for col in EXCEL_COLUMNS}
    merged.update({k: v for k, v in patch_record.items() if k in EXCEL_COLUMNS})

    drive_id  = item["parentReference"]["driveId"]
    item_id   = item["id"]
    row_index = employee["_row_index"]
    _write_row_patch(token, drive_id, item_id, row_index, object_to_row(merged))
    return merged
