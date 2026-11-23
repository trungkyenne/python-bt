# -*- coding: utf-8 -*-
r"""
Bài 01: Tính chu vi và diện tích hình chữ nhật
Mức độ: Dễ
Mục tiêu: Viết chương trình yêu cầu người dùng nhập vào chiều dài và chiều rộng của một hình chữ nhật (là các số thực dương). Hãy tính chu vi và diện tích của hình chữ nhật đó, sau đó in kết quả ra màn hình với độ chính xác lấy 2 chữ số thập phân.
"""

# Nhập chiều dài và chiều rộng từ bàn phím
a = float(input("Nhập chiều dài: "))
b = float(input("Nhập chiều rộng: "))

# Tính chu vi và diện tích
chu_vi = 2 * (a + b)
dien_tich = a * b

# In kết quả định dạng 2 chữ số thập phân
print(f"Chu vi: {chu_vi:.2f}")
print(f"Dien tich: {dien_tich:.2f}")
