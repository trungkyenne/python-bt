# -*- coding: utf-8 -*-
r"""
Bài 13: Tính tổng dãy số nguyên liên tiếp từ 1 đến N
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một số nguyên dương $N$. Hãy tính và in ra tổng $S = 1 + 2 + 3 + \dots + N$ bằng cách sử dụng vòng lặp `for`. Không dùng công thức toán học $N(N+1)/2$ để tính trực tiếp.
"""

n = int(input("Nhập N: "))

tong = 0
for i in range(1, n + 1):
    tong += i

print(f"Tong: {tong}")
