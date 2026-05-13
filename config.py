import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
TENANT_ID = os.getenv("TENANT_ID", "common")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:5000/auth/callback")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-me")
SCOPES = ["User.Read", "Files.ReadWrite"]
EXCEL_TABLE_NAME = os.getenv("EXCEL_TABLE_NAME", "EmployeeTable")

# Path to the folder in the owner's OneDrive (relative to drive root)
ONEDRIVE_FOLDER = os.getenv(
    "ONEDRIVE_FOLDER",
    "Documents/1. Project/CSA (Center of Skill Acquisition)/New Operator Monitoring",
)

# IMPORTANT: Please verify that each SharePoint link matches the correct workbook.
# The mapping below follows the order provided in the conversation: EA, G1, G2, G3, G4, TRM.
DEPARTMENTS = {
    "EA": {
        "label": "EA",
        "workbook_name": "CSA Monitoring Report_EA_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQCT8Ik6tm_rSJ74kTZpfy5nAVos858uy90ZcKh2ajlWPB4?e=CwjthY",
    },
    "G1": {
        "label": "G1",
        "workbook_name": "CSA Monitoring Report_G1_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQBvE30PLadSQr3LxorbUVCDAYkih4UTNzoTu7xMLBBIr1U?e=m8v1bM",
    },
    "G2": {
        "label": "G2",
        "workbook_name": "CSA Monitoring Report_G2_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQA7PyY-Blu6QZoUTidEdXlnAVw87EyIUbAxqt9i4kLZeJc?e=osIuby",
    },
    "G3": {
        "label": "G3",
        "workbook_name": "CSA Monitoring Report_G3_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQCbi16Hfi5jSJhsMM3MYlTTAUdRxCDJEHEzLigMS8ohZE0?e=UgUVof",
    },
    "G4": {
        "label": "G4",
        "workbook_name": "CSA Monitoring Report_G4_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQDYQRWEAzS3SLy5FIeGEsbuAWzehRjHwFcwkxE62sGwl8g?e=bfQn9r",
    },
    "TRM": {
        "label": "TRM",
        "workbook_name": "CSA Monitoring Report_TRM_for App.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQA9cQHFhe21QJTuQoaPl6bSAX5x_EwSQixheBTD3KlQBD8?e=guj06d",
    },
}

EXCEL_COLUMNS = [
    "ID",
    "Employee ID",
    "Employee Name",
    "Grade",
    "Week",
    "CSA Start Date",
    "Due date",
    "Operation End (week)",
    "3 Days Resign",
    "Remaining days (working days)",
    "Non - Working Days",
    "Due date (week)",
    "Basic Start",
    "Basic End",
    "Operation Start",
    "Operation End",
    "Resign Date",
    "Transfers Date",
    "Graduate Eff",
    "On time",
    "Actual Status",
    "Comment",
    "Employees Leave",
    "Review",
    "Total Training Days",
]

GRADE_ALLOWED_WORKING_DAYS = {
    "B": 18,
    "C": 6,
    "D": 5,
    "E": 2,
}
