# -*- coding: utf-8 -*-
r"""
Bài 29: Kiểm tra số hoàn hảo (Perfect Number)
Mức độ: Trung bình
Mục tiêu: Số hoàn hảo là số nguyên dương mà tổng các ước số nguyên dương thực sự của nó (tức các ước số nhỏ hơn chính nó) bằng chính nó. Ví dụ: $6 = 1 + 2 + 3$. Viết chương trình nhập số nguyên dương $N$ và kiểm tra xem $N$ có phải là số hoàn hảo hay không.
"""

n = int(input("Nhập N: "))

if n <= 1:
    print("Khong phai so hoan hao")
else:
    tong_uoc = 1 # 1 luôn là ước thực sự
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i:
                tong_uoc += n // i
                
    if tong_uoc == n:
        print("So hoan hao")
    else:
        print("Khong phai so hoan hao")
