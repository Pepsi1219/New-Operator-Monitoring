import base64
import requests
from config import EXCEL_COLUMNS, EXCEL_TABLE_NAME

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


def get_drive_item(token, share_url):
    share_id = encode_sharing_url(share_url)
    return graph_request(
        token,
        "GET",
        f"/shares/{share_id}/driveItem",
        headers={**_headers(token), "Prefer": "redeemSharingLinkIfNecessary"},
    )


def row_to_object(values):
    values = values or []
    return {column: values[index] if index < len(values) else "" for index, column in enumerate(EXCEL_COLUMNS)}


def object_to_row(record):
    return [record.get(column, "") for column in EXCEL_COLUMNS]


def get_table_rows(token, department):
    item = get_drive_item(token, department["share_url"])
    drive_id = item["parentReference"]["driveId"]
    item_id = item["id"]
    data = graph_request(token, "GET", f"/drives/{drive_id}/items/{item_id}/workbook/tables/{EXCEL_TABLE_NAME}/rows")
    rows = data.get("value", [])
    employees = []
    for index, row in enumerate(rows):
        values = (row.get("values") or [[]])[0]
        obj = row_to_object(values)
        emp_id = str(obj.get("Employee ID", "")).strip()
        if emp_id and emp_id != "0":
            obj["_row_index"] = index
            employees.append(obj)
    return item, employees


def find_employee(token, department, employee_id):
    _, employees = get_table_rows(token, department)
    employee_id = str(employee_id or "").strip()
    for employee in employees:
        if str(employee.get("Employee ID", "")).strip() == employee_id:
            return employee
    return None


def create_employee(token, department, record):
    item, employees = get_table_rows(token, department)
    employee_id = str(record.get("Employee ID", "")).strip()
    if not employee_id:
        raise GraphExcelError("Employee ID is required")
    if any(str(emp.get("Employee ID", "")).strip() == employee_id for emp in employees):
        raise GraphExcelError(f"Employee ID {employee_id} already exists")

    current_ids = []
    for emp in employees:
        try:
            current_ids.append(int(float(emp.get("ID", 0))))
        except (ValueError, TypeError):
            pass
    next_id = max(current_ids or [0]) + 1

    new_record = {column: "" for column in EXCEL_COLUMNS}
    new_record.update(record)
    new_record["ID"] = next_id
    new_record["Actual Status"] = "Under basic"

    drive_id = item["parentReference"]["driveId"]
    item_id = item["id"]
    body = {"index": None, "values": [object_to_row(new_record)]}
    graph_request(token, "POST", f"/drives/{drive_id}/items/{item_id}/workbook/tables/{EXCEL_TABLE_NAME}/rows/add", json=body)
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

    merged = {column: employee.get(column, "") for column in EXCEL_COLUMNS}
    merged.update({k: v for k, v in patch_record.items() if k in EXCEL_COLUMNS})
    merged["Employee ID"] = employee.get("Employee ID", employee_id)

    drive_id = item["parentReference"]["driveId"]
    item_id = item["id"]
    row_index = employee["_row_index"]

    body = {"values": [object_to_row(merged)]}
    # Update the exact Excel table row range. This avoids creating duplicate rows.
    graph_request(
        token,
        "PATCH",
        f"/drives/{drive_id}/items/{item_id}/workbook/tables/{EXCEL_TABLE_NAME}/rows/itemAt(index={row_index})/range",
        json=body,
    )
    return merged
