# -*- coding: utf-8 -*-
r"""
Bài 23: Tính giá trị số pi xấp xỉ theo chuỗi Leibniz
Mức độ: Khó
Mục tiêu: Công thức chuỗi Leibniz dùng để tính xấp xỉ số $\pi$ như sau:\n$\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \dots + \frac{(-1)^n}{2n+1}$.\nViết chương trình nhập vào số nguyên dương $N$ là số lượng số hạng của chuỗi. Hãy tính và in ra giá trị xấp xỉ của $\pi$ lấy 6 chữ số thập phân.
"""

n = int(input("Nhập số lượng số hạng N: "))

sum_s = 0.0
for i in range(n):
    term = 1.0 / (2 * i + 1)
    if i % 2 == 0:
        sum_s += term
    else:
        sum_s -= term

pi_approx = 4 * sum_s
print(f"Pi xap xi: {pi_approx:.6f}")
