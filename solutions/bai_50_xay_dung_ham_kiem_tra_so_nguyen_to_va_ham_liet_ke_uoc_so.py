# -*- coding: utf-8 -*-
r"""
Bài 50: Xây dựng hàm kiểm tra số nguyên tố và hàm liệt kê ước số
Mức độ: Dễ
Mục tiêu: Hãy thiết kế hai hàm:
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

# Chương trình chính
n = int(input("Nhập n: "))
print(f"So nguyen to: {is_prime(n)}")
print(f"Cac uoc so: {' '.join(map(str, get_divisors(n)))}")
