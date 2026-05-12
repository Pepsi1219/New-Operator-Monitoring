# New Operator Monitoring - Python Version

Web App เวอร์ชัน Python Flask สำหรับอ่าน/เขียน Excel บน SharePoint ผ่าน Microsoft Graph API

## โครงสร้างไฟล์

```text
new-operator-monitoring-python/
├─ app.py                  # Flask routes + Microsoft login + API
├─ config.py               # ค่า config, Department mapping, Excel columns
├─ graph_excel.py          # อ่าน/เขียน Excel ผ่าน Microsoft Graph
├─ business_rules.py       # คำนวณ Due date / Remaining days / Status
├─ requirements.txt        # Python dependencies
├─ .env.example            # ตัวอย่าง Environment variables
├─ templates/
│  └─ index.html           # HTML หลัก
└─ static/
   ├─ css/
   │  └─ styles.css        # CSS
   └─ js/
      └─ app.js            # Frontend JavaScript
```

## สิ่งที่ต้องเตรียมใน Excel

Excel ทั้ง 6 ไฟล์ต้องมี Table ชื่อ `EmployeeTable` บน sheet `data`

Column ต้องเรียงตามนี้:

```text
ID, Employee ID, Employee Name, Grade, Week, CSA Start Date, Due date, Operation End (week), 3 Days Resign, Remaining days (working days), Non - Working Days, Due date (week), Basic Start, Basic End, Operation Start, Operation End, Resign Date, Transfers Date, Graduate Eff, On time, Actual Status, Comment, Employees Leave, Review, Total Training Days
```

ถ้าใน Excel ยังเป็น range ธรรมดา:

1. เปิดไฟล์ Excel Online
2. ไปที่ sheet `data`
3. เลือกหัวตาราง + ข้อมูลทั้งหมด
4. Insert > Table
5. Table Design > Table Name = `EmployeeTable`

## สร้าง Microsoft Entra App Registration

1. เข้า Microsoft Entra admin center
2. App registrations > New registration
3. Name: `New Operator Monitoring`
4. Supported account types: Single tenant / This organizational directory only
5. Redirect URI: Web = `http://localhost:5000/auth/callback`
6. Copy `Application (client) ID`
7. Copy `Directory (tenant) ID`
8. Certificates & secrets > New client secret
9. API permissions > Add delegated permissions:
   - `User.Read`
   - `Files.ReadWrite`
10. ถ้าองค์กรบังคับ ให้ Admin กด Grant admin consent

## วิธีรัน

```bash
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate # macOS/Linux

pip install -r requirements.txt
copy .env.example .env      # Windows
# cp .env.example .env      # macOS/Linux
```

แก้ไขไฟล์ `.env`:

```env
CLIENT_ID=ใส่ Client ID
CLIENT_SECRET=ใส่ Client Secret
TENANT_ID=ใส่ Tenant ID
REDIRECT_URI=http://localhost:5000/auth/callback
FLASK_SECRET_KEY=ตั้งค่า random ยาวๆ
EXCEL_TABLE_NAME=EmployeeTable
```

รัน:

```bash
python app.py
```

เปิดเว็บ:

```text
http://localhost:5000
```

## หมายเหตุสำคัญ

- ระบบนี้ไม่ต้องใช้ Node.js
- ใช้ Python Flask เป็น Backend
- แยกไฟล์ HTML / CSS / JS ชัดเจน
- ใช้ Microsoft Graph API อ่าน/เขียน Excel บน SharePoint
- วันหยุดพิเศษเก็บใน Browser Local Storage ก่อนในเวอร์ชัน MVP
- ก่อนใช้งานจริง กรุณาตรวจสอบ mapping ลิงก์ Excel ใน `config.py` ว่าตรงกับ EA/G1/G2/G3/G4/TRM จริง
