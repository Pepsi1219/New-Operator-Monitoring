// ===== TRANSLATIONS =====
const TRANSLATIONS = {
  th: {
    appTitle:               'New Operator Monitoring',
    appSubtitle:            'ระบบติดตามข้อมูลพนักงานใหม่',
    loginTitle:             'เข้าสู่ระบบด้วย Microsoft Account',
    loginDesc:              'ระบบนี้ใช้ Microsoft Graph เพื่ออ่าน/เขียน Excel บน SharePoint ขององค์กร',
    loginBtn:               'Sign in with Microsoft',
    selectDept:             'เลือกหน่วยงาน',
    adminTitle:             'ตั้งค่าผู้ดูแลระบบ',
    holidaySection:         'กำหนดวันหยุดพิเศษ',
    addHoliday:             'เพิ่มวันหยุด',
    holidayHint:            'ระบบจะไม่นับวันอาทิตย์และวันหยุดพิเศษในการคำนวณ Remaining Days',
    backHome:               '← กลับหน้าแรก',
    refresh:                'โหลดใหม่',
    total:                  'ทั้งหมด',
    congratulations:        'สำเร็จการฝึก',
    training:               'กำลังฝึก',
    resignation:            'การลาออก',
    register:               'ลงทะเบียน',
    newRecord:              'บันทึกข้อมูลใหม่',
    employeeId:             'รหัสพนักงาน',
    employeeName:           'ชื่อพนักงาน',
    grade:                  'เกรด',
    selectPlaceholder:      '-- เลือก --',
    saveNew:                'บันทึกพนักงานใหม่',
    viewEdit:               'ดูข้อมูล / แก้ไขข้อมูล',
    search:                 'ค้นหา',
    remaining:              'คงเหลือ',
    workingDays:            'วันทำงาน',
    csaStartDate:           'CSA Start Date',
    basicStart:             'Basic Start',
    basicEnd:               'Basic End',
    operationStart:         'Operation Start',
    operationEnd:           'Operation End',
    resignDate:             'วันลาออก',
    transfersDate:          'วันโอนย้าย',
    graduateEff:            'Graduate Eff',
    comment:                'หมายเหตุ',
    saveUpdate:             'บันทึกการแก้ไข',
    close:                  'ปิด',
    riskList:               'ข้อมูลพนักงาน',
    filterAll:              'ทั้งหมด',
    colEmployeeId:          'รหัสพนักงาน',
    colEmployeeName:        'ชื่อพนักงาน',
    colGrade:               'เกรด',
    colCsaStart:            'วันเริ่มฝึก',
    colDueDate:             'วันครบกำหนด',
    colBasicStart:          'เริ่มฝึกพื้นฐาน',
    colBasicEnd:            'ฝึกพื้นฐานเสร็จ',
    colOpStart:             'เริ่มฝึกขั้นตอนงาน',
    colOpEnd:               'ฝึกขั้นตอนงานเสร็จ',
    colResignDate:          'วันลาออก',
    colTransferDate:        'วันโอนย้าย',
    colGradEff:             'ประสิทธิภาพ',
    colActualStatus:        'สถานะจริง',
    dashboard:              'แดชบอร์ด',
    dueDate:                'Due Date',
    employeeIdPlaceholder:  'รหัสพนักงาน',
    signedIn:               'เข้าสู่ระบบแล้ว',
    logout:                 'ออกจากระบบ',
    loading:                'กำลังโหลด...',
    loadedCount:            'โหลด {n} พนักงาน',
    created:                'สร้างพนักงานใหม่สำเร็จ',
    updated:                'อัปเดตข้อมูลสำเร็จ',
    loaded:                 'โหลดข้อมูลพนักงานสำเร็จ',
    pleaseEnterEmployeeId:  'กรุณากรอกรหัสพนักงาน',
    statusCompleted:        'ฝึกเสร็จ',
    statusCompletedOverdue: 'ฝึกเสร็จ (เกินกำหนด)',
    statusUnderOperation:   'กำลังฝึกขั้นตอนงาน',
    statusUnderBasic:       'กำลังฝึกพื้นฐาน',
    statusResignOperation:  'ลาออกระหว่างฝึกขั้นตอน',
    statusResignBasic:      'ลาออกระหว่างฝึกพื้นฐาน',
    statusTransferOperation:'โอนย้ายระหว่างฝึกขั้นตอน',
    statusTransferBasic:    'โอนย้ายระหว่างฝึกพื้นฐาน',
  },
  en: {
    appTitle:               'New Operator Monitoring',
    appSubtitle:            'New employee tracking system',
    loginTitle:             'Sign in with Microsoft Account',
    loginDesc:              'This system uses Microsoft Graph to read/write Excel files on SharePoint.',
    loginBtn:               'Sign in with Microsoft',
    selectDept:             'Select Department',
    adminTitle:             'Admin Settings',
    holidaySection:         'Configure Special Holidays',
    addHoliday:             'Add Holiday',
    holidayHint:            'Sundays and special holidays are excluded from the Remaining Days calculation.',
    backHome:               '← Back to Home',
    refresh:                'Refresh',
    total:                  'Total',
    congratulations:        'Completed Training',
    training:               'In Training',
    resignation:            'Resignation',
    register:               'Register',
    newRecord:              'Create New Record',
    employeeId:             'Employee ID',
    employeeName:           'Employee Name',
    grade:                  'Grade',
    selectPlaceholder:      '-- Select --',
    saveNew:                'Save New Employee',
    viewEdit:               'View / Edit Record',
    search:                 'Search',
    remaining:              'Remaining',
    workingDays:            'working days',
    csaStartDate:           'CSA Start Date',
    basicStart:             'Basic Start',
    basicEnd:               'Basic End',
    operationStart:         'Operation Start',
    operationEnd:           'Operation End',
    resignDate:             'Resign Date',
    transfersDate:          'Transfers Date',
    graduateEff:            'Graduate Eff',
    comment:                'Comment',
    saveUpdate:             'Save Update',
    close:                  'Close',
    riskList:               'Employee Data',
    filterAll:              'All',
    colEmployeeId:          'Employee ID',
    colEmployeeName:        'Employee Name',
    colGrade:               'Grade',
    colCsaStart:            'CSA Start',
    colDueDate:             'Due Date',
    colBasicStart:          'Basic Start',
    colBasicEnd:            'Basic End',
    colOpStart:             'Op Start',
    colOpEnd:               'Op End',
    colResignDate:          'Resign Date',
    colTransferDate:        'Transfer Date',
    colGradEff:             'Eff%',
    colActualStatus:        'Actual Status',
    dashboard:              'Dashboard',
    dueDate:                'Due Date',
    employeeIdPlaceholder:  'Employee ID',
    signedIn:               'Signed in',
    logout:                 'Logout',
    loading:                'Loading...',
    loadedCount:            'Loaded {n} employees',
    created:                'Employee created successfully',
    updated:                'Employee updated successfully',
    loaded:                 'Employee data loaded',
    pleaseEnterEmployeeId:  'Please enter Employee ID',
    statusCompleted:        'Completed',
    statusCompletedOverdue: 'Completed (Overdue)',
    statusUnderOperation:   'In Operation Training',
    statusUnderBasic:       'In Basic Training',
    statusResignOperation:  'Resigned (Op Training)',
    statusResignBasic:      'Resigned (Basic Training)',
    statusTransferOperation:'Transferred (Op Training)',
    statusTransferBasic:    'Transferred (Basic Training)',
  },
  lo: {
    appTitle:               'New Operator Monitoring',
    appSubtitle:            'ລະບົບຕິດຕາມພະນັກງານໃໝ່',
    loginTitle:             'ເຂົ້າສູ່ລະບົບດ້ວຍ Microsoft Account',
    loginDesc:              'ລະບົບນີ້ໃຊ້ Microsoft Graph ເພື່ອອ່ານ/ຂຽນ Excel ເທິງ SharePoint ຂອງອົງກອນ',
    loginBtn:               'Sign in with Microsoft',
    selectDept:             'ເລືອກພະແນກ',
    adminTitle:             'ຕັ້ງຄ່າຜູ້ດູແລລະບົບ',
    holidaySection:         'ກຳນົດວັນຫຍຸດພິເສດ',
    addHoliday:             'ເພີ່ມວັນຫຍຸດ',
    holidayHint:            'ລະບົບຈະບໍ່ນັບວັນອາທິດ ແລະ ວັນຫຍຸດພິເສດໃນການຄຳນວນ Remaining Days',
    backHome:               '← ກັບໄປໜ້າຫຼັກ',
    refresh:                'ໂຫຼດໃໝ່',
    total:                  'ທັງໝົດ',
    congratulations:        'ສຳເລັດການຝຶກ',
    training:               'ກຳລັງຝຶກ',
    resignation:            'ການລາອອກ',
    register:               'ລົງທະບຽນ',
    newRecord:              'ບັນທຶກຂໍ້ມູນໃໝ່',
    employeeId:             'ລະຫັດພະນັກງານ',
    employeeName:           'ຊື່ພະນັກງານ',
    grade:                  'ເກຣດ',
    selectPlaceholder:      '-- ເລືອກ --',
    saveNew:                'ບັນທຶກພະນັກງານໃໝ່',
    viewEdit:               'ເບິ່ງ / ແກ້ໄຂຂໍ້ມູນ',
    search:                 'ຄົ້ນຫາ',
    remaining:              'ຄົງເຫຼືອ',
    workingDays:            'ວັນເຮັດວຽກ',
    csaStartDate:           'CSA Start Date',
    basicStart:             'Basic Start',
    basicEnd:               'Basic End',
    operationStart:         'Operation Start',
    operationEnd:           'Operation End',
    resignDate:             'ວັນລາອອກ',
    transfersDate:          'ວັນໂອນຍ້າຍ',
    graduateEff:            'Graduate Eff',
    comment:                'ໝາຍເຫດ',
    saveUpdate:             'ບັນທຶກການແກ້ໄຂ',
    close:                  'ປິດ',
    riskList:               'ຂໍ້ມູນພະນັກງານ',
    filterAll:              'ທັງໝົດ',
    colEmployeeId:          'ລະຫັດພະນັກງານ',
    colEmployeeName:        'ຊື່ພະນັກງານ',
    colGrade:               'ເກຣດ',
    colCsaStart:            'ວັນເລີ່ມຝຶກ',
    colDueDate:             'ວັນຄົບກຳນົດ',
    colBasicStart:          'ເລີ່ມຝຶກພື້ນຖານ',
    colBasicEnd:            'ຝຶກພື້ນຖານສຳເລັດ',
    colOpStart:             'ເລີ່ມຝຶກຂັ້ນຕອນ',
    colOpEnd:               'ຝຶກຂັ້ນຕອນສຳເລັດ',
    colResignDate:          'ວັນລາອອກ',
    colTransferDate:        'ວັນໂອນຍ້າຍ',
    colGradEff:             'ປະສິດທິພາບ',
    colActualStatus:        'ສະຖານະຈິງ',
    dashboard:              'ແດສບອດ',
    dueDate:                'Due Date',
    employeeIdPlaceholder:  'ລະຫັດພະນັກງານ',
    signedIn:               'ເຂົ້າສູ່ລະບົບແລ້ວ',
    logout:                 'ອອກຈາກລະບົບ',
    loading:                'ກຳລັງໂຫຼດ...',
    loadedCount:            'ໂຫຼດ {n} ພະນັກງານ',
    created:                'ສ້າງພະນັກງານໃໝ່ສຳເລັດ',
    updated:                'ອັບເດດຂໍ້ມູນສຳເລັດ',
    loaded:                 'ໂຫຼດຂໍ້ມູນພະນັກງານສຳເລັດ',
    pleaseEnterEmployeeId:  'ກະລຸນາໃສ່ລະຫັດພະນັກງານ',
    statusCompleted:        'ຝຶກສຳເລັດ',
    statusCompletedOverdue: 'ຝຶກສຳເລັດ (ເກີນກຳນົດ)',
    statusUnderOperation:   'ກຳລັງຝຶກຂັ້ນຕອນ',
    statusUnderBasic:       'ກຳລັງຝຶກພື້ນຖານ',
    statusResignOperation:  'ລາອອກລະຫວ່າງຝຶກຂັ້ນຕອນ',
    statusResignBasic:      'ລາອອກລະຫວ່າງຝຶກພື້ນຖານ',
    statusTransferOperation:'ໂອນຍ້າຍລະຫວ່າງຝຶກຂັ້ນຕອນ',
    statusTransferBasic:    'ໂອນຍ້າຍລະຫວ່າງຝຶກພື້ນຖານ',
  },
  vi: {
    appTitle:               'New Operator Monitoring',
    appSubtitle:            'Hệ thống theo dõi nhân viên mới',
    loginTitle:             'Đăng nhập bằng tài khoản Microsoft',
    loginDesc:              'Hệ thống này sử dụng Microsoft Graph để đọc/ghi Excel trên SharePoint của tổ chức.',
    loginBtn:               'Sign in with Microsoft',
    selectDept:             'Chọn bộ phận',
    adminTitle:             'Cài đặt Admin',
    holidaySection:         'Cấu hình ngày nghỉ đặc biệt',
    addHoliday:             'Thêm ngày nghỉ',
    holidayHint:            'Hệ thống sẽ không tính Chủ nhật và ngày nghỉ đặc biệt khi tính Remaining Days.',
    backHome:               '← Về trang chủ',
    refresh:                'Làm mới',
    total:                  'Tổng',
    congratulations:        'Hoàn thành đào tạo',
    training:               'Đang đào tạo',
    resignation:            'Nghỉ việc',
    register:               'Đăng ký',
    newRecord:              'Tạo bản ghi mới',
    employeeId:             'Mã nhân viên',
    employeeName:           'Tên nhân viên',
    grade:                  'Cấp bậc',
    selectPlaceholder:      '-- Chọn --',
    saveNew:                'Lưu nhân viên mới',
    viewEdit:               'Xem / Chỉnh sửa',
    search:                 'Tìm kiếm',
    remaining:              'Còn lại',
    workingDays:            'ngày làm việc',
    csaStartDate:           'CSA Start Date',
    basicStart:             'Basic Start',
    basicEnd:               'Basic End',
    operationStart:         'Operation Start',
    operationEnd:           'Operation End',
    resignDate:             'Ngày nghỉ việc',
    transfersDate:          'Ngày chuyển',
    graduateEff:            'Graduate Eff',
    comment:                'Ghi chú',
    saveUpdate:             'Lưu cập nhật',
    close:                  'Đóng',
    riskList:               'Dữ liệu nhân viên',
    filterAll:              'Tất cả',
    colEmployeeId:          'Mã nhân viên',
    colEmployeeName:        'Tên nhân viên',
    colGrade:               'Cấp bậc',
    colCsaStart:            'Ngày bắt đầu',
    colDueDate:             'Ngày hết hạn',
    colBasicStart:          'Bắt đầu cơ bản',
    colBasicEnd:            'Kết thúc cơ bản',
    colOpStart:             'Bắt đầu vận hành',
    colOpEnd:               'Kết thúc vận hành',
    colResignDate:          'Ngày nghỉ',
    colTransferDate:        'Ngày chuyển',
    colGradEff:             'Hiệu suất',
    colActualStatus:        'Trạng thái thực',
    dashboard:              'Bảng điều khiển',
    dueDate:                'Ngày hết hạn',
    employeeIdPlaceholder:  'Mã nhân viên',
    signedIn:               'Đã đăng nhập',
    logout:                 'Đăng xuất',
    loading:                'Đang tải...',
    loadedCount:            'Đã tải {n} nhân viên',
    created:                'Tạo nhân viên mới thành công',
    updated:                'Cập nhật thông tin thành công',
    loaded:                 'Đã tải dữ liệu nhân viên',
    pleaseEnterEmployeeId:  'Vui lòng nhập mã nhân viên',
    statusCompleted:        'Hoàn thành',
    statusCompletedOverdue: 'Hoàn thành (Trễ hạn)',
    statusUnderOperation:   'Đang đào tạo vận hành',
    statusUnderBasic:       'Đang đào tạo cơ bản',
    statusResignOperation:  'Nghỉ việc (Đào tạo vận hành)',
    statusResignBasic:      'Nghỉ việc (Đào tạo cơ bản)',
    statusTransferOperation:'Chuyển bộ phận (Vận hành)',
    statusTransferBasic:    'Chuyển bộ phận (Cơ bản)',
  },
};

// ===== STATE =====
let currentDepartment = null;
let currentEmployeeId = null;
let currentFilter     = '';
let departments       = [];
let holidays          = JSON.parse(localStorage.getItem('specialHolidays') || '[]');
let lastEmployees     = [];
let currentUser       = null;
let lastCalc          = null;
let currentLang       = localStorage.getItem('lang')  || 'th';
let currentTheme      = localStorage.getItem('theme') || 'light';

const $ = (id) => document.getElementById(id);

// ===== TRANSLATION HELPERS =====
function t(key, vars = {}) {
  const lang = TRANSLATIONS[currentLang] || TRANSLATIONS.en;
  let val = lang[key] ?? TRANSLATIONS.en[key] ?? key;
  if (typeof val === 'string' && vars.n !== undefined) {
    val = val.replace('{n}', vars.n);
  }
  return String(val);
}

function applyTranslations() {
  document.querySelectorAll('[data-i18n]').forEach(el => {
    el.textContent = t(el.dataset.i18n);
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    el.placeholder = t(el.dataset.i18nPlaceholder);
  });
  document.documentElement.lang = currentLang;
}

// ===== STATUS HELPERS =====
const STATUS_KEY_MAP = {
  'completed':            'statusCompleted',
  'completed-overdue':    'statusCompletedOverdue',
  'under-operation':      'statusUnderOperation',
  'under-basic':          'statusUnderBasic',
  'resign-operation':     'statusResignOperation',
  'resign-basic':         'statusResignBasic',
  'transfer-operation':   'statusTransferOperation',
  'transfer-basic':       'statusTransferBasic',
};

function statusBadgeClass(key) {
  if (key === 'completed')                                   return 'ok';
  if (key === 'completed-overdue')                           return 'warn';
  if (key === 'under-operation' || key === 'under-basic')    return 'warn';
  if (key === 'resign-operation' || key === 'resign-basic')  return 'danger';
  if (key === 'transfer-operation' || key === 'transfer-basic') return 'muted';
  return 'muted';
}

// ===== THEME =====
function applyTheme(theme) {
  currentTheme = theme;
  document.documentElement.dataset.theme = theme;
  $('themeToggle').textContent = theme === 'dark' ? '☀️' : '🌙';
  localStorage.setItem('theme', theme);
}

function initTheme() {
  applyTheme(currentTheme);
  $('themeToggle').onclick = () => applyTheme(currentTheme === 'dark' ? 'light' : 'dark');
}

// ===== LANGUAGE =====
function initLang() {
  const sel = $('langSelect');
  sel.value = currentLang;
  applyTranslations();

  sel.onchange = () => {
    currentLang = sel.value;
    localStorage.setItem('lang', currentLang);
    applyTranslations();
    if (currentDepartment) {
      const dep = departments.find(d => d.key === currentDepartment);
      if (dep) $('dashboardTitle').textContent = `${dep.label} ${t('dashboard')}`;
    }
    if (lastEmployees.length) renderEmployeeTable(lastEmployees);
    if (currentUser) {
      $('authBox').innerHTML = `${t('signedIn')} · <a href="/logout">${t('logout')}</a>`;
    }
    if (lastCalc) {
      $('dueDateText').textContent = `${t('dueDate')}: ${lastCalc.due_date || '-'}`;
    }
  };
}

// ===== ADMIN FAB / MODAL =====
function initAdmin() {
  $('adminBtn').onclick = () => $('adminModal').classList.remove('hidden');
  $('closeAdminBtn').onclick = closeAdmin;
  $('adminModal').onclick = (e) => { if (e.target === $('adminModal')) closeAdmin(); };
}
function closeAdmin() { $('adminModal').classList.add('hidden'); }

// ===== REGISTER MODAL =====
function initRegisterModal() {
  $('registerBtn').onclick    = () => $('registerModal').classList.remove('hidden');
  $('closeRegisterBtn').onclick = closeRegisterModal;
  $('registerModal').onclick  = (e) => { if (e.target === $('registerModal')) closeRegisterModal(); };
  $('createBtn').onclick      = createNewEmployee;
}
function closeRegisterModal() { $('registerModal').classList.add('hidden'); }

// ===== EDIT MODAL =====
function initEditModal() {
  $('closeEditModalBtn').onclick = closeEditModal;
  $('closeEditBtn').onclick      = closeEditModal;
  $('editModal').onclick = (e) => { if (e.target === $('editModal')) closeEditModal(); };
  $('editForm').onsubmit = saveEditForm;
}
function closeEditModal() { $('editModal').classList.add('hidden'); }

// ===== UTILITY =====
function show(el) { el.classList.remove('hidden'); }
function hide(el) { el.classList.add('hidden'); }

function showMessage(text, isError = false) {
  const box = $('messageBox');
  box.textContent = text;
  box.style.borderLeftColor = isError ? '#b42318' : '#e5b300';
  show(box);
}

function getHolidayQuery() {
  return holidays.map(h => `holiday=${encodeURIComponent(h)}`).join('&');
}

async function api(path, options = {}) {
  const res = await fetch(path, {
    ...options,
    headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) throw new Error(data.error || `Request failed: ${res.status}`);
  return data;
}

function normalizeDateForInput(value) {
  if (value === null || value === undefined || value === '' || value === 0) return '';
  if (typeof value === 'number') {
    if (value <= 0) return '';
    // Excel serial date: days since Dec 30, 1899
    const d = new Date(Date.UTC(1899, 11, 30) + Math.round(value) * 86400000);
    return isNaN(d.getTime()) ? '' : d.toISOString().slice(0, 10);
  }
  const str = String(value).trim();
  if (!str) return '';
  const d = new Date(str);
  if (isNaN(d.getTime())) return str.slice(0, 10);
  return d.toISOString().slice(0, 10);
}

// ===== HOLIDAYS =====
function renderHolidays() {
  const list = $('holidayList');
  list.innerHTML = '';
  holidays.forEach(date => {
    const chip = document.createElement('span');
    chip.className = 'chip';
    chip.innerHTML = `${date} <button type="button">×</button>`;
    chip.querySelector('button').onclick = () => {
      holidays = holidays.filter(h => h !== date);
      localStorage.setItem('specialHolidays', JSON.stringify(holidays));
      renderHolidays();
      if (currentDepartment) loadDashboard();
    };
    list.appendChild(chip);
  });
}

// ===== PAGES =====
function setPage(page) {
  hide($('homePage'));
  hide($('dashboardPage'));
  if (page === 'home')      show($('homePage'));
  if (page === 'dashboard') show($('dashboardPage'));
}

// ===== DEPARTMENT GRID =====
function renderDepartmentButtons() {
  const grid = $('departmentGrid');
  grid.innerHTML = '';
  departments.forEach(dep => {
    const btn = document.createElement('button');
    btn.className = 'department-btn';
    btn.innerHTML = `${dep.label}<small>${dep.workbook_name}</small>`;
    btn.onclick = () => {
      currentDepartment = dep.key;
      $('dashboardTitle').textContent = `${dep.label} ${t('dashboard')}`;
      setPage('dashboard');
      loadDashboard();
    };
    grid.appendChild(btn);
  });
}

// ===== COMPUTE ACTUAL STATUS =====
function computeActualStatus(emp, calc) {
  function hasData(v) {
    return v !== null && v !== undefined && v !== '' && v !== 0;
  }
  const opStart    = emp['Operation Start'];
  const opEnd      = emp['Operation End'];
  const basicStart = emp['Basic Start'];
  const resignDate = emp['Resign Date'];
  const transferDate = emp['Transfers Date'];
  const dueDate    = (calc && calc.due_date) ? calc.due_date : '';

  if (hasData(opEnd)) {
    const opEndNorm = normalizeDateForInput(opEnd);
    if (dueDate && opEndNorm && opEndNorm > dueDate) return 'completed-overdue';
    return 'completed';
  }
  if (hasData(resignDate) && hasData(opStart))    return 'resign-operation';
  if (hasData(resignDate) && hasData(basicStart)) return 'resign-basic';
  if (hasData(transferDate) && hasData(opStart))    return 'transfer-operation';
  if (hasData(transferDate) && hasData(basicStart)) return 'transfer-basic';
  if (hasData(opStart))    return 'under-operation';
  if (hasData(basicStart)) return 'under-basic';
  return 'under-basic';
}

// ===== EMPLOYEE TABLE =====
function buildRowHTML(emp, calc, actualKey) {
  const nd = (v) => normalizeDateForInput(v) || '';
  const gradEff = (emp['Graduate Eff'] !== undefined && emp['Graduate Eff'] !== '') ? emp['Graduate Eff'] : '';
  const badgeClass = statusBadgeClass(actualKey);
  const statusLabel = t(STATUS_KEY_MAP[actualKey] || actualKey);
  const empId = String(emp['Employee ID'] || '').replace(/"/g, '&quot;');

  return `
    <td><button class="btn-row-edit" data-id="${empId}" title="Edit">✏</button></td>
    <td>${emp['Employee ID']   || ''}</td>
    <td>${emp['Employee Name'] || ''}</td>
    <td>${emp['Grade']         || ''}</td>
    <td>${nd(emp['CSA Start Date'])}</td>
    <td>${calc.due_date        || ''}</td>
    <td>${nd(emp['Basic Start'])}</td>
    <td>${nd(emp['Basic End'])}</td>
    <td>${nd(emp['Operation Start'])}</td>
    <td>${nd(emp['Operation End'])}</td>
    <td>${nd(emp['Resign Date'])}</td>
    <td>${nd(emp['Transfers Date'])}</td>
    <td>${gradEff}</td>
    <td><span class="badge ${badgeClass}">${statusLabel}</span></td>
  `;
}

function renderEmployeeTable(employees) {
  const body = $('employeeTableBody');
  body.innerHTML = '';

  let total = employees.length;
  let completed = 0, underOp = 0, underBasic = 0, resignOp = 0, resignBasic = 0;

  employees.forEach(emp => {
    const calc = emp.calculated || {};
    const actualKey = computeActualStatus(emp, calc);

    if (actualKey === 'completed' || actualKey === 'completed-overdue') completed++;
    else if (actualKey === 'under-operation')  underOp++;
    else if (actualKey === 'under-basic')      underBasic++;
    else if (actualKey === 'resign-operation') resignOp++;
    else if (actualKey === 'resign-basic')     resignBasic++;

    // Apply filter
    if (currentFilter && actualKey !== currentFilter) return;

    const tr = document.createElement('tr');
    tr.className = `actual-${actualKey}`;
    tr.dataset.employeeId = emp['Employee ID'] || '';
    tr.innerHTML = buildRowHTML(emp, calc, actualKey);
    body.appendChild(tr);
  });

  $('totalCount').textContent      = total;
  $('onTrackCount').textContent    = completed;
  $('trainingCount').textContent   = underOp + underBasic;
  $('underOpCount').textContent    = underOp;
  $('underBasicCount').textContent = underBasic;
  $('overdueCount').textContent    = resignOp + resignBasic;
  $('resignOpCount').textContent   = resignOp;
  $('resignBasicCount').textContent = resignBasic;
}

// ===== DASHBOARD =====
async function loadDashboard() {
  if (!currentDepartment) return;
  showMessage(t('loading'));
  try {
    const query = getHolidayQuery();
    const data = await api(`/api/${currentDepartment}/employees${query ? '?' + query : ''}`);
    lastEmployees = data.employees || [];
    renderEmployeeTable(lastEmployees);
    showMessage(t('loadedCount', { n: lastEmployees.length }));
  } catch (err) {
    if (err.message && err.message.includes('login_required')) {
      show($('loginPanel'));
      setPage('home');
    } else {
      showMessage(err.message, true);
    }
  }
}

// ===== OPEN EDIT MODAL =====
async function openEditModal(employeeId) {
  currentEmployeeId = employeeId;
  try {
    const query = getHolidayQuery();
    const emp = await api(
      `/api/${currentDepartment}/employees/${encodeURIComponent(employeeId)}${query ? '?' + query : ''}`
    );
    fillEditForm(emp);
    show($('editModal'));
  } catch (err) {
    showMessage(err.message, true);
  }
}

// ===== CREATE EMPLOYEE =====
async function createNewEmployee() {
  const payload = {
    'Employee ID':    $('newEmployeeId').value.trim(),
    'Employee Name':  $('newEmployeeName').value.trim(),
    'CSA Start Date': $('newCsaStartDate').value,
  };
  if (!payload['Employee ID']) {
    showMessage(t('pleaseEnterEmployeeId'), true);
    return;
  }
  try {
    await api(`/api/${currentDepartment}/employees`, { method: 'POST', body: JSON.stringify(payload) });
    $('newEmployeeId').value   = '';
    $('newEmployeeName').value = '';
    $('newCsaStartDate').value = '';
    closeRegisterModal();
    showMessage(t('created'));
    loadDashboard();
  } catch (err) {
    showMessage(err.message, true);
  }
}

// ===== SEARCH EMPLOYEE =====
async function searchEmployee() {
  const empId = $('searchEmployeeId').value.trim();
  if (!empId) return showMessage(t('pleaseEnterEmployeeId'), true);
  await openEditModal(empId);
}

// ===== EDIT FORM =====
function fillEditForm(emp) {
  const form   = $('editForm');
  const fields = [
    'Employee ID', 'Employee Name', 'Grade',
    'CSA Start Date', 'Basic Start', 'Basic End',
    'Operation Start', 'Operation End', 'Resign Date',
    'Transfers Date', 'Graduate Eff', 'Comment',
  ];
  fields.forEach(name => {
    const input = form.elements[name];
    if (!input) return;
    input.value = input.type === 'date' ? normalizeDateForInput(emp[name]) : (emp[name] || '');
  });

  const calc = emp.calculated || {};
  lastCalc = calc;
  $('statusBadge').textContent   = t(STATUS_KEY_MAP[computeActualStatus(emp, calc)] || '');
  $('statusBadge').className     = `badge ${statusBadgeClass(computeActualStatus(emp, calc))}`;
  $('remainingDays').textContent = calc.remaining_days ?? '-';
  $('progressBar').style.width   = `${calc.progress || 0}%`;
  $('dueDateText').textContent   = `${t('dueDate')}: ${calc.due_date || '-'}`;
}

async function saveEditForm(event) {
  event.preventDefault();
  const form     = $('editForm');
  const formData = new FormData(form);
  const payload  = {};
  for (const [key, value] of formData.entries()) payload[key] = value;
  payload._holidays = holidays;

  try {
    const data = await api(
      `/api/${currentDepartment}/employees/${encodeURIComponent(currentEmployeeId)}`,
      { method: 'PATCH', body: JSON.stringify(payload) }
    );
    fillEditForm(data.employee);
    showMessage(t('updated'));
    loadDashboard();
  } catch (err) {
    showMessage(err.message, true);
  }
}

// ===== INIT =====
async function init() {
  initTheme();
  initLang();
  initAdmin();
  initRegisterModal();
  initEditModal();

  // Status filter
  $('statusFilter').onchange = () => {
    currentFilter = $('statusFilter').value;
    renderEmployeeTable(lastEmployees);
  };

  // Holiday add button
  $('addHolidayBtn').onclick = () => {
    const value = $('holidayInput').value;
    if (value && !holidays.includes(value)) {
      holidays.push(value);
      holidays.sort();
      localStorage.setItem('specialHolidays', JSON.stringify(holidays));
      $('holidayInput').value = '';
      renderHolidays();
    }
  };

  // Navigation buttons
  $('backHomeBtn').onclick = () => setPage('home');
  $('refreshBtn').onclick  = loadDashboard;
  $('searchBtn').onclick   = searchEmployee;

  // Row edit button (event delegation)
  $('employeeTableBody').addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-row-edit');
    if (!btn) return;
    const empId = btn.dataset.id;
    if (empId) openEditModal(empId);
  });

  // Check auth
  const me = await api('/api/me');
  if (!me.authenticated) {
    show($('loginPanel'));
    return;
  }

  currentUser = me.user;
  $('authBox').innerHTML = `${t('signedIn')} · <a href="/logout">${t('logout')}</a>`;
  show($('adminBtn'));

  departments = await api('/api/departments');
  if (!Array.isArray(departments)) departments = [];
  renderDepartmentButtons();
  renderHolidays();
  setPage('home');
}

init().catch(err => {
  console.error(err);
  show($('loginPanel'));
});
