# -*- coding: utf-8 -*-
r"""
Bài 51: Xây dựng hàm tính giai thừa và hàm tính tổ hợp chập K của N
Mức độ: Trung bình
Mục tiêu: Công thức tính tổ hợp chập $k$ của $n$ phần tử là: $C(n, k) = \frac{n!}{k!(n-k)!}$ ($0 \le k \le n$).\nHãy xây dựng:
"""

def factorial(num):
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

def combination(n, k):
    if k < 0 or k > n:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

# Chương trình chính
n, k = map(int, input("Nhập n k: ").split())
print(f"C(n, k) = {combination(n, k)}")
