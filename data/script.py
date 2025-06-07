# import pandas as pd
# import numpy as np
# import pytz
# from datetime import datetime, timedelta

# # Thiết lập timezone Việt Nam
# tz = pytz.timezone('Asia/Ho_Chi_Minh')

# # Số lượng dòng dữ liệu muốn sinh (sửa tùy nhu cầu)
# num_rows = 1001  

# # Ngày hôm nay
# now = datetime.now()  # không có timezone


# # Tạo danh sách thời gian check_in ngẫu nhiên trong 3 tháng gần nhất
# check_in_dates = [
#     tz.localize(now - timedelta(days=np.random.randint(0, 90), hours=np.random.randint(0, 24), minutes=np.random.randint(0, 60)))
#     for _ in range(num_rows)
# ]

# # Sinh check_out cách 1–5 ngày sau check_in
# check_out_dates = [
#     check_in + timedelta(days=np.random.randint(1, 6), hours=np.random.randint(0, 12))
#     for check_in in check_in_dates
# ]

# # Tạo DataFrame mới
# df = pd.DataFrame({
#     'check_in': check_in_dates,
#     'check_out': check_out_dates
# })

# # Ghi ra file CSV giữ timezone (theo định dạng ISO)
# df.to_csv("data/appointments2.csv", index=False)

# print("✅ Đã tạo dữ liệu ảo check_in/check_out thành công.")


import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pytz

tz = pytz.timezone('Asia/Ho_Chi_Minh')
num_rows = 100  # Số dòng dữ liệu

now = datetime.now()

# Tạo created_at ngẫu nhiên trong 2 năm gần nhất
created_at_list = [
    tz.localize(now - timedelta(days=np.random.randint(0, 730),  # 2 năm = 730 ngày
                                hours=np.random.randint(0, 24),
                                minutes=np.random.randint(0, 60),
                                seconds=np.random.randint(0, 60)))
    for _ in range(num_rows)
]

# updated_at sau created_at vài giờ đến vài ngày
updated_at_list = [
    created_at + timedelta(days=np.random.randint(0, 10),
                           hours=np.random.randint(0, 12),
                           minutes=np.random.randint(0, 60),
                           seconds=np.random.randint(0, 60))
    for created_at in created_at_list
]

# Xuất DataFrame
df = pd.DataFrame({
    'created_at': created_at_list,
    'updated_at': updated_at_list
})

# Ghi ra file CSV
df.to_csv("data/created_updated_at.csv", index=False)
print("✅ Đã tạo dữ liệu thời gian thực tế với timezone và quan hệ hợp lý.")
