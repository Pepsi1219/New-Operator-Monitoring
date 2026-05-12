import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
TENANT_ID = os.getenv("TENANT_ID", "common")
AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
REDIRECT_URI = os.getenv("REDIRECT_URI", "http://localhost:5000/auth/callback")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-me")
SCOPES = ["User.Read", "Files.ReadWrite", "offline_access"]
EXCEL_TABLE_NAME = os.getenv("EXCEL_TABLE_NAME", "EmployeeTable")

# IMPORTANT: Please verify that each SharePoint link matches the correct workbook.
# The mapping below follows the order provided in the conversation: EA, G1, G2, G3, G4, TRM.
DEPARTMENTS = {
    "EA": {
        "label": "EA",
        "workbook_name": "CSA Monitoring Report - EA.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQC9iSVzebbkQKSRk_rFT30ZAY4gWVB6Nne9NucYx-yzvSQ?e=A1GJmn",
    },
    "G1": {
        "label": "G1",
        "workbook_name": "CSA Monitoring Report - G1.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQBXUjJ7Aaw6QLpf24GPpToIAXWMlcWNU1riKN79C-JZy4Q?e=7fpVKn",
    },
    "G2": {
        "label": "G2",
        "workbook_name": "CSA Monitoring Report - G2.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQBrcX8gIlsUSpbxxVYbZEy-AXfN802R7GsZSRIFqd9ZKTE?e=Esg16s",
    },
    "G3": {
        "label": "G3",
        "workbook_name": "CSA Monitoring Report - G3.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQB3MoD7mfUGQJH0X1ySVSK_AV5jCvU8oGpV0eElKgySHsM?e=mfmqgK",
    },
    "G4": {
        "label": "G4",
        "workbook_name": "CSA Monitoring Report - G4.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQB564pmpeGKSKu4CbXrGd6AAdLjhF-tFrB15uoSN526b6M?e=HefbUZ",
    },
    "TRM": {
        "label": "TRM",
        "workbook_name": "CSA Monitoring Report - TRM.xlsx",
        "share_url": "https://nanyangtextilegroup-my.sharepoint.com/:x:/g/personal/pongsathon_s_nanyangtextile_com/IQCcmztv3Ba2SLAi9z71Yy7WAaPsXXstA24uC_Nl-B5ppSk?e=TZePUV",
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
