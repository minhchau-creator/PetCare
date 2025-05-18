  
  
  // Xử lý menu dropdown user ở header
  const userMenuBtn = document.getElementById('userMenuBtn');
  const userDropdown = document.getElementById('userDropdown');
  userMenuBtn.addEventListener('click', () => {
    const expanded = userMenuBtn.getAttribute('aria-expanded') === 'true';
    userMenuBtn.setAttribute('aria-expanded', !expanded);
    userDropdown.style.display = expanded ? 'none' : 'flex';
  });

  // Đóng dropdown khi click ra ngoài
  document.addEventListener('click', (event) => {
    if (!userMenuBtn.contains(event.target) && !userDropdown.contains(event.target)) {
      userDropdown.style.display = 'none';
      userMenuBtn.setAttribute('aria-expanded', 'false');
    }
  });

  // Sidebar menu mở submenu Lịch hẹn
  const lichHenMenu = document.getElementById('lichHenMenu');
  const lichHenSubmenu = document.getElementById('lichHenSubmenu');

  lichHenMenu.addEventListener('click', (e) => {
    e.preventDefault();
    const isVisible = lichHenSubmenu.style.display === 'block';
    if (isVisible) {
      lichHenSubmenu.style.display = 'none';
      lichHenMenu.classList.remove('dropdown-active');
    } else {
      lichHenSubmenu.style.display = 'block';
      lichHenMenu.classList.add('dropdown-active');
    }
  });



  //form thêm lịch hẹn
 function showSection(event) {
    event.preventDefault(); // Ngăn form submit mặc định

    const form = document.getElementById('them-lichhen-form');
    if (form) {
        const elements = form.querySelectorAll('input, select, textarea');
        let message = '🔔 Thông tin bạn đã nhập:\n\n';

        elements.forEach(el => {
            if (el.type === 'submit' || el.type === 'hidden' || el.type === 'button') return;

            // Tìm label gần nhất (trước hoặc cùng cấp cha)
            let label = '';
            const formGroup = el.closest('.form-group');
            if (formGroup) {
                const labelEl = formGroup.querySelector('label');
                if (labelEl) {
                    label = labelEl.textContent.trim();
                }
            }

            let value = el.value.trim();

            // Với select thì lấy text của option được chọn
            if (el.tagName.toLowerCase() === 'select') {
                const selectedOption = el.options[el.selectedIndex];
                if (selectedOption) {
                    value = selectedOption.text.trim();
                }
            }

            if (label) {
                message += `${label}: ${value}\n`;
            }
        });

        alert(message); // Hiển thị thông tin
    }

    // Ẩn form
    document.getElementById('them-lichhen').classList.add('hidden');

    // Chuyển hướng sang trang danh sách lịch hẹn
    window.location.href = 'danhsachlichhen.html';
}


function closeForm() {
    document.getElementById('them-lichhen').classList.add('hidden');
}


// CALENDAR 


// const Calendar = tui.Calendar;

// const calendar = new Calendar('#calendar', {
//   defaultView: 'week',
//   taskView: true,
//   scheduleView: true,
//   useDetailPopup: true,
//   useFormPopup: true
// });

// // Thêm một sự kiện mẫu
// calendar.createEvents([
//   {
//     id: '1',
//     calendarId: '1',
//     title: 'Họp nhóm',
//     category: 'time',
//     start: '2025-05-19T10:30:00',
//     end: '2025-05-19T12:30:00',
//   },
//   {
//     id: '2',
//     calendarId: '1',
//     title: 'Khám thú cưng',
//     category: 'time',
//     start: '2025-05-20T09:00:00',
//     end: '2025-05-20T10:00:00',
//   }
// ]);






// function formatTime(datetime) {
//   const date = new Date(datetime);
//   const hours = String(date.getHours()).padStart(2, '0');
//   const minutes = String(date.getMinutes()).padStart(2, '0');
//   return `${hours}:${minutes}`;
// }

// const calendar = new tui.Calendar('#calendar', {
//   defaultView: 'week',
//   useCreationPopup: true, // BẬT lên để sử dụng hook beforeCreateSchedule
//   template: {
//     time(event) {
//       const { start, end, title } = event;
//       return `<span style="color: white;">${formatTime(start)}~${formatTime(end)} ${title}</span>`;
//     },
//     allday(event) {
//       return `<span style="color: gray;">${event.title}</span>`;
//     },
//   },
//   calendars: [
//     {
//       id: 'cal1',
//       name: 'Personal',
//       backgroundColor: '#03bd9e',
//     },
//     {
//       id: 'cal2',
//       name: 'Work',
//       backgroundColor: '#00a9ff',
//     },
//   ],
// });



// // Tạo element form ẩn sẵn trong body
// const formHTML = `
//   <div id="scheduleForm" style="display:none; position:fixed; top:50%; left:50%; 
//       transform: translate(-50%, -50%); background:white; padding:20px; border-radius:8px;
//       box-shadow:0 0 10px rgba(0,0,0,0.3); z-index: 9999;">
//     <h3>Thêm lịch mới</h3>
//     <form id="newScheduleForm">
//       <label>Tiêu đề:<br><input type="text" name="title" required></label><br><br>
//       <label>Thời gian bắt đầu:<br><input type="datetime-local" name="start" required></label><br><br>
//       <label>Thời gian kết thúc:<br><input type="datetime-local" name="end" required></label><br><br>
//       <button type="submit">Thêm lịch</button>
//       <button type="button" id="cancelBtn">Hủy</button>
//     </form>
//   </div>
//   <div id="overlay" style="display:none; position:fixed; top:0; left:0; width:100vw; height:100vh; 
//     background: rgba(0,0,0,0.3); z-index:9998;"></div>
// `;
// document.body.insertAdjacentHTML('beforeend', formHTML);

// const scheduleForm = document.getElementById('scheduleForm');
// const overlay = document.getElementById('overlay');
// const newScheduleForm = document.getElementById('newScheduleForm');
// const cancelBtn = document.getElementById('cancelBtn');

// // Hàm hiện form và overlay
// function openForm(start, end) {
//   scheduleForm.style.display = 'block';
//   overlay.style.display = 'block';

//   // Gán giá trị thời gian mặc định cho input
//   newScheduleForm.start.value = start ? start.toISOString().slice(0,16) : '';
//   newScheduleForm.end.value = end ? end.toISOString().slice(0,16) : '';
//   newScheduleForm.title.value = '';
// }

// // Ẩn form và overlay
// function closeForm() {
//   scheduleForm.style.display = 'none';
//   overlay.style.display = 'none';
// }

// cancelBtn.addEventListener('click', closeForm);
// overlay.addEventListener('click', closeForm);

// // Bắt sự kiện click vào khung thời gian trong calendar
// calendar.on('clickSchedule', (event) => {
//   console.log('Đã click vào lịch:', event);
// });



// // Xử lý submit form tạo lịch mới
// newScheduleForm.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const title = newScheduleForm.title.value.trim();
//   const start = new Date(newScheduleForm.start.value);
//   const end = new Date(newScheduleForm.end.value);

//   if (title && start && end && end > start) {
//     calendar.createSchedules([{
//       id: String(Date.now()),
//       calendarId: 'cal1',
//       title: title,
//       category: 'time',
//       start: start.toISOString(),
//       end: end.toISOString(),
//       color: '#fff',
//       bgColor: '#03bd9e',
//     }]);
//     closeForm();
//   } else {
//     alert('Vui lòng nhập đúng thông tin lịch và thời gian kết thúc phải lớn hơn bắt đầu.');
//   }
// });


function formatTime(datetime) {
  const date = new Date(datetime);
  const hours = String(date.getHours()).padStart(2, '0');
  const minutes = String(date.getMinutes()).padStart(2, '0');
  return `${hours}:${minutes}`;
}

const calendar = new tui.Calendar('#calendar', {
  defaultView: 'week',
  useCreationPopup: false, // Tắt popup mặc định
  template: {
    time(event) {
      const { start, end, title } = event;
      return `<span style="color: white;">${formatTime(start)}~${formatTime(end)} ${title}</span>`;
    },
    allday(event) {
      return `<span style="color: gray;">${event.title}</span>`;
    },
  },
  calendars: [
    {
      id: 'cal1',
      name: 'Personal',
      backgroundColor: '#03bd9e',
    },
    {
      id: 'cal2',
      name: 'Work',
      backgroundColor: '#00a9ff',
    },
  ],
});
