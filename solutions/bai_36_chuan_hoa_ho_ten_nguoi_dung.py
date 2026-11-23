# -*- coding: utf-8 -*-
r"""
Bài 36: Chuẩn hóa họ tên người dùng
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một chuỗi họ và tên người dùng bị lỗi định dạng (có thể chứa khoảng trắng thừa ở đầu, cuối hoặc giữa các từ, chữ cái viết hoa thường lộn xộn). Hãy chuẩn hóa chuỗi họ tên đó theo quy tắc: Không có khoảng cách thừa ở đầu và cuối, giữa các từ chỉ có đúng 1 khoảng cách, và chữ cái đầu mỗi từ viết hoa, các chữ cái còn lại viết thường.
"""

s = input("Nhập họ tên cần chuẩn hóa: ")

words = s.split()
chuan_hoa_words = [w.capitalize() for w in words]
ho_ten_chuan = " ".join(chuan_hoa_words)

print(f"Ho ten chuan: {ho_ten_chuan}")
