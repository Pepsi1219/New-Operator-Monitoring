from datetime import date, datetime, timedelta
from config import GRADE_ALLOWED_WORKING_DAYS


def parse_date(value):
    """Parse dates from HTML input, ISO strings, or Excel-like strings."""
    if value in (None, "", 0):
        return None
    if isinstance(value, date) and not isinstance(value, datetime):
        return value
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, (int, float)):
        # Excel serial date, epoch 1899-12-30
        return date(1899, 12, 30) + timedelta(days=int(value))

    text = str(value).strip()
    if not text:
        return None

    formats = ["%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    try:
        return datetime.fromisoformat(text).date()
    except ValueError:
        return None


def iso(value):
    parsed = parse_date(value)
    return parsed.isoformat() if parsed else ""


def normalize_holidays(holidays):
    return {iso(h) for h in (holidays or []) if iso(h)}


def is_working_day(day, holidays=None):
    holidays = normalize_holidays(holidays)
    # Python weekday: Monday=0 ... Sunday=6
    if day.weekday() == 6:
        return False
    if day.isoformat() in holidays:
        return False
    return True


def add_working_days(start_date, working_days, holidays=None):
    start = parse_date(start_date)
    if not start or not working_days:
        return None
    current = start
    count = 0
    while count < working_days:
        current += timedelta(days=1)
        if is_working_day(current, holidays):
            count += 1
    return current


def working_days_between(start_date, end_date, holidays=None):
    start = parse_date(start_date)
    end = parse_date(end_date)
    if not start or not end:
        return None

    if start == end:
        return 0

    direction = 1 if start < end else -1
    current = start
    count = 0

    while current != end:
        current += timedelta(days=direction)
        if is_working_day(current, holidays):
            count += direction
    return count


def calculate_due_date(operation_start, grade, holidays=None):
    grade = str(grade or "").upper().strip()
    allowed = GRADE_ALLOWED_WORKING_DAYS.get(grade)
    if not operation_start or not allowed:
        return None
    return add_working_days(operation_start, allowed, holidays)


def calculate_status(record, holidays=None, today=None):
    today = today or date.today()
    grade = str(record.get("Grade", "")).upper().strip()
    operation_start = record.get("Operation Start")
    operation_end = record.get("Operation End")
    resign_date = record.get("Resign Date")
    transfer_date = record.get("Transfers Date")

    due_date = calculate_due_date(operation_start, grade, holidays)
    allowed_days = GRADE_ALLOWED_WORKING_DAYS.get(grade)
    remaining_days = working_days_between(today, due_date, holidays) if due_date else None

    if parse_date(resign_date):
        status = "Resigned"
    elif parse_date(transfer_date):
        status = "Transferred"
    elif parse_date(operation_end):
        status = "Completed"
    elif remaining_days is None:
        status = "Not Started"
    elif remaining_days <= 0:
        status = "Overdue"
    elif remaining_days <= 2:
        status = "Warning"
    else:
        status = "On Track"

    used_days = None
    progress = 0
    if allowed_days and remaining_days is not None:
        used_days = max(0, allowed_days - max(0, remaining_days))
        progress = min(100, max(0, round((used_days / allowed_days) * 100, 1)))

    on_time = ""
    if parse_date(operation_end) and due_date:
        on_time = "Y" if parse_date(operation_end) <= due_date else "N"

    return {
        "due_date": iso(due_date),
        "remaining_days": remaining_days,
        "allowed_days": allowed_days,
        "used_days": used_days,
        "progress": progress,
        "status": status,
        "on_time": on_time,
    }
