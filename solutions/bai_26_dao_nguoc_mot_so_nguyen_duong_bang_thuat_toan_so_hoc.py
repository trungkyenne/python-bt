# -*- coding: utf-8 -*-
r"""
Bài 26: Đảo ngược một số nguyên dương bằng thuật toán số học
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào số nguyên dương $N$. Hãy tìm số đảo ngược của $N$ và in ra màn hình. Yêu cầu: Sử dụng thuật toán toán học (chia nguyên `//` và chia dư `%`), không sử dụng thủ thuật đảo chuỗi `str(n)[::-1]`.
"""

n = int(input("Nhập số nguyên dương N: "))

temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

print(f"So dao nguoc: {rev}")
