# -*- coding: utf-8 -*-
r"""
Bài 22: Vẽ tam giác cân đặc đối xứng chiều cao H
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào số nguyên dương $H$ biểu diễn chiều cao của tam giác cân. Hãy in ra tam giác cân đối xứng gồm các ký tự sao `*`. Dòng thứ $i$ ($i = 1, 2, \dots, H$) có $H - i$ khoảng trắng ở đầu và $2i - 1$ ký tự `*`.
"""

h = int(input("Nhập chiều cao H: "))

for i in range(1, h + 1):
    khoang_trang = " " * (h - i)
    sao = "*" * (2 * i - 1)
    print(khoang_trang + sao)
