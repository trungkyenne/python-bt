# -*- coding: utf-8 -*-
r"""
Bài 14: In bảng cửu chương của một số nguyên K
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào số nguyên $K$ ($1 \le K \le 9$). Hãy in bảng nhân của số $K$ từ 1 đến 10 theo định dạng chuẩn: `K x i = <tích>`.
"""

k = int(input("Nhập K (1-9): "))

for i in range(1, 11):
    print(f"{k} x {i} = {k * i}")
