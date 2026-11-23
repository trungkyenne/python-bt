# -*- coding: utf-8 -*-
r"""
Bài 03: Tính tiền lương thực lĩnh của nhân viên
Mức độ: Trung bình
Mục tiêu: Một công ty tính lương nhân viên dựa trên số giờ làm việc trong tháng và lương theo giờ. Lương cơ bản bằng số giờ làm việc nhân với đơn giá mỗi giờ. Nhân viên phải đóng 10.5% bảo hiểm bắt buộc và 5% thuế thu nhập cá nhân trên lương cơ bản. Hãy viết chương trình nhập số giờ làm và đơn giá giờ, tính và in ra Lương cơ bản, Tổng tiền khấu trừ và Lương thực lĩnh.
"""

# Nhập số giờ làm và lương giờ
so_gio = float(input("Nhập số giờ làm: "))
don_gia = float(input("Nhập đơn giá mỗi giờ: "))

# Tính các thành phần lương
luong_cb = so_gio * don_gia
khau_tru = luong_cb * (0.105 + 0.05)
thuc_linh = luong_cb - khau_tru

# Hiển thị kết quả
print(f"Luong co ban: {luong_cb:.2f}")
print(f"Khau tru: {khau_tru:.2f}")
print(f"Thuc linh: {thuc_linh:.2f}")
