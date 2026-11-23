# -*- coding: utf-8 -*-
r"""
Bài 20: Vẽ hình tam giác vuông ký tự sao (*) kích thước N
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào số nguyên dương $N$ ($1 \le N \le 20$). Hãy in ra tam giác vuông cân gồm các ký tự sao `*` có cạnh góc vuông bằng $N$, góc vuông ở góc dưới bên trái.
"""

n = int(input("Nhập N: "))

for i in range(1, n + 1):
    print("*" * i)
