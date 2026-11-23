# -*- coding: utf-8 -*-
r"""
Bài 21: Vẽ hình chữ nhật rỗng kích thước M x N
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào hai số nguyên dương $M$ (số hàng) và $N$ (số cột) với $M, N \ge 2$. Hãy in ra hình chữ nhật rỗng kích thước $M \times N$ được tạo bởi các ký tự sao `*` viền ngoài và khoảng trắng ` ` ở bên trong.
"""

m, n = map(int, input("Nhập số hàng M và số cột N: ").split())

for i in range(m):
    if i == 0 or i == m - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")
