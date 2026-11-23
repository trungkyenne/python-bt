# -*- coding: utf-8 -*-
r"""
Bài 25: Tính tổng và số lượng các chữ số của một số nguyên dương
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một số nguyên dương $N$. Hãy tính và in ra số lượng chữ số và tổng các chữ số của $N$ bằng các phép toán số học chia lấy phần nguyên `//` và chia lấy phần dư `%`. Không xử lý ép kiểu chuỗi string.
"""

n = int(input("Nhập số nguyên dương N: "))

temp = n
so_luong = 0
tong_cs = 0

while temp > 0:
    chu_so = temp % 10
    tong_cs += chu_so
    so_luong += 1
    temp //= 10

print(f"So luong chu so: {so_luong}")
print(f"Tong chu so: {tong_cs}")
