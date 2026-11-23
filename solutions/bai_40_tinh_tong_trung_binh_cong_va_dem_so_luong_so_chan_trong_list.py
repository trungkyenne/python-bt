# -*- coding: utf-8 -*-
r"""
Bài 40: Tính tổng, trung bình cộng và đếm số lượng số chẵn trong List
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên từ bàn phím trên một dòng (cách nhau bởi khoảng trắng). Hãy tính và in ra: Tổng các phần tử, Giá trị trung bình cộng (lấy 2 chữ số thập phân) và Số lượng các số chẵn có trong danh sách.
"""

nums = list(map(int, input("Nhập danh sách số: ").split()))

tong = 0
so_chan = 0

for x in nums:
    tong += x
    if x % 2 == 0:
        so_chan += 1

tb = tong / len(nums)

print(f"Tong: {tong}")
print(f"Trung binh: {tb:.2f}")
print(f"So luong so chan: {so_chan}")
