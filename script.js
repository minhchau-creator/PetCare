  
  
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
                if (el.type === 'submit' || el.type === 'hidden') return;

                let label = el.placeholder || '';
                if (el.tagName.toLowerCase() === 'select') {
                    const firstOption = el.querySelector('option');
                    if (firstOption && firstOption.value === '') {
                        label = firstOption.textContent.trim();
                    }
                }

                let value = el.value.trim();
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

        // Ẩn form (nếu muốn giữ)
        document.getElementById('them-lichhen').classList.add('hidden');

        // Chuyển hướng sang trang danh sách lịch hẹn
        window.location.href = 'danhsachlichhen.html';
    }


function closeForm() {
    document.getElementById('them-lichhen').classList.add('hidden');
}

