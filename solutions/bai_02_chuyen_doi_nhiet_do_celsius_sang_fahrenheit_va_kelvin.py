# -*- coding: utf-8 -*-
r"""
Bài 02: Chuyển đổi nhiệt độ Celsius sang Fahrenheit và Kelvin
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào giá trị nhiệt độ theo thang đo Celsius ($^\circ C$). Hãy chuyển đổi và in ra nhiệt độ tương ứng theo thang đo Fahrenheit ($^\circ F$) và Kelvin ($K$).
"""

# Nhập nhiệt độ Celsius
c = float(input("Nhập độ C: "))

# Chuyển đổi công thức
f = c * 1.8 + 32
k = c + 273.15

# Xuất kết quả
print(f"Fahrenheit: {f:.2f}")
print(f"Kelvin: {k:.2f}")
