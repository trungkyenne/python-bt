# -*- coding: utf-8 -*-
r"""
Bài 18: Tính giá trị số mũ $A^B$ bằng vòng lặp không dùng toán tử **
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào số thực $A$ và số nguyên không âm $B$. Hãy tính giá trị lũy thừa $A^B$ bằng vòng lặp. Yêu cầu: Không sử dụng toán tử lũy thừa `**` và không dùng hàm `pow()`.
"""

a = float(input("Nhập cơ số A: "))
b = int(input("Nhập số mũ B: "))

res = 1.0
for _ in range(b):
    res *= a

print(f"{res:.4f}")
