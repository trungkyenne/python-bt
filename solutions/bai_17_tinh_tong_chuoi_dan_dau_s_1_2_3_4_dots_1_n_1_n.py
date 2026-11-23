# -*- coding: utf-8 -*-
r"""
Bài 17: Tính tổng chuỗi đan dấu $S = 1 - 2 + 3 - 4 + \dots + (-1)^{N-1}N$
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào số nguyên dương $N$. Hãy tính giá trị của biểu thức chuỗi đan dấu: $S = 1 - 2 + 3 - 4 + 5 - \dots + (-1)^{N-1}N$. Sử dụng vòng lặp.
"""

n = int(input("Nhập N: "))

tong_s = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        tong_s += i
    else:
        tong_s -= i

print(f"Tong S: {tong_s}")
