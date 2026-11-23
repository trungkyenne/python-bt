# -*- coding: utf-8 -*-
r"""
Bài 32: Tìm ước số chung lớn nhất (UCLN) và bội số chung nhỏ nhất (BCNN)
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào hai số nguyên dương $a$ và $b$. Hãy tìm và in ra Ước chung lớn nhất (UCLN) bằng thuật toán Euclid và Bội chung nhỏ nhất (BCNN) của hai số đó mà không dùng thư viện `math`.
"""

a, b = map(int, input("Nhập hai số a b: ").split())

orig_a, orig_b = a, b

# Thuật toán Euclid
x, y = a, b
while y != 0:
    x, y = y, x % y

ucln = x
bcnn = (orig_a * orig_b) // ucln

print(f"UCLN: {ucln}")
print(f"BCNN: {bcnn}")
