  
  
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

// const calendar = new tui.Calendar('#calendar', {
//   defaultView: 'month', // có thể đổi thành 'week' hoặc 'day' khi khởi tạo
//   taskView: false,
//   scheduleView: ['time'], // chỉ hiện phần time (không hiện all-day)
//   useCreationPopup: true,  // bật popup tạo lịch
//   useDetailPopup: true,    // bật popup chi tiết lịch
//   template: {
//     popupSave: () => 'Lưu',
//     popupEdit: () => 'Sửa',
//     popupDelete: () => 'Xoá',
//     popupTitle: () => 'Tiêu đề',
//     popupLocation: () => 'Địa điểm',
//     popupStartDate: () => 'Bắt đầu',
//     popupEndDate: () => 'Kết thúc',
//     timegridDisplayPrimaryTime: function(time) {
//       return `${time.getHours()}:00`;  // định dạng giờ cho week và day view
//     }
//   },
//   week: {
//     hourStart: 8,
//     hourEnd: 20,
//     hourHeight: 50
//   },
//   calendars: [
//     {
//       id: 'lichhen',
//       name: 'Lịch hẹn',
//       backgroundColor: '#9e5fff',
//       borderColor: '#9e5fff'
//     }
//   ],
//   // Thêm phần view để bật 3 chế độ xem
//   // Khi có header, người dùng sẽ tự chuyển qua lại
//   // Bạn cần có phần header ngoài để điều khiển view hoặc gọi api calendar.changeView()
//   view: {
//     month: true,
//     week: true,
//     day: true
//   }
// });


// // Sự kiện khi người dùng nhấn thêm lịch
// calendar.on('beforeCreateSchedule', function(event) {
//   const { start, end, title, location } = event;
//   calendar.createSchedules([{
//     id: String(Date.now()), // ID tạm thời
//     calendarId: 'lichhen',
//     title: title,
//     location: location,
//     start: start,
//     end: end,
//     category: 'time'
//   }]);
// });

// // Sự kiện khi nhấn vào lịch đã tạo
// calendar.on('clickSchedule', function(event) {
//   const schedule = event.schedule;
//   alert(`Bạn đã chọn lịch: ${schedule.title}\nĐịa điểm: ${schedule.location}`);
// });

// CALENDAR 



function formatTime(datetime) {
    const date = new Date(datetime);
    const hours = String(date.getHours()).padStart(2, '0');
    const minutes = String(date.getMinutes()).padStart(2, '0');
    return `${hours}:${minutes}`;
  }


const calendar = new tui.Calendar('#calendar', {
  defaultView: 'week',
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

calendar.createSchedules([
  {
    id: '1',
    calendarId: 'cal1', // ✅ sửa lại
    title: 'Yoga',
    category: 'time',
    start: '2025-05-12T06:30:00',
    end: '2025-05-12T07:30:00',
    color: '#fff',
    bgColor: '#33cc33'
  },
  {
    id: '2',
    calendarId: 'cal2', // ✅ sửa lại
    title: 'Writing',
    category: 'time',
    start: '2025-05-12T09:00:00',
    end: '2025-05-12T12:00:00',
    color: '#fff',
    bgColor: '#e60000'
  },
  {
    id: '3',
    calendarId: 'cal1', // ✅ sửa lại
    title: 'Email',
    category: 'time',
    start: '2025-05-12T12:00:00',
    end: '2025-05-12T13:00:00',
    color: '#fff',
    bgColor: '#3366cc'
  }
]);
