# -*- coding: utf-8 -*-
r"""
Bài 16: Đếm và tính tổng các ước số nguyên dương của N
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào số nguyên dương $N$. Hãy tìm tất cả các ước số nguyên dương của $N$, đếm số lượng ước và tính tổng tất cả các ước số đó.
"""

n = int(input("Nhập N: "))

cac_uoc = []
tong_uoc = 0

for i in range(1, n + 1):
    if n % i == 0:
        cac_uoc.append(str(i))
        tong_uoc += i

print(" ".join(cac_uoc))
print(f"So luong uoc: {len(cac_uoc)}")
print(f"Tong cac uoc: {tong_uoc}")
