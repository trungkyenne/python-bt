# -*- coding: utf-8 -*-
r"""
Bài 04: Chuyển đổi thời gian từ giây sang giờ, phút, giây
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một số nguyên dương $T$ đại diện cho số giây. Hãy chuyển đổi số giây trên thành định dạng chuẩn Giờ : Phút : Giây theo cú pháp `HH:MM:SS` (mỗi thành phần có 2 chữ số, nếu nhỏ hơn 10 thì chèn số 0 ở đầu).
"""

# Nhập số giây nguyên
t = int(input("Nhập tổng số giây: "))

# Phân rã giờ, phút, giây bằng phép chia nguyên và chia dư
gio = t // 3600
phut = (t % 3600) // 60
giay = t % 60

# In ra định dạng HH:MM:SS
print(f"{gio:02d}:{phut:02d}:{giay:02d}")
