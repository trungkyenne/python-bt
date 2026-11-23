# -*- coding: utf-8 -*-
r"""
Bài 42: Tìm phần tử lớn thứ hai trong danh sách
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên. Hãy tìm phần tử có giá trị lớn thứ hai trong danh sách (giá trị lớn thứ hai phải thực sự nhỏ hơn giá trị lớn nhất). Nếu danh sách không có phần tử lớn thứ hai (tất cả các phần tử bằng nhau hoặc danh sách có ít hơn 2 phần tử), in ra thông báo 'Khong ton tai'. Không sử dụng hàm sắp xếp `sort()`.
"""

nums = list(map(int, input("Nhập danh sách số: ").split()))

first = None
second = None

for x in nums:
    if first is None or x > first:
        second = first
        first = x
    elif x < first:
        if second is None or x > second:
            second = x

if second is None:
    print("Khong ton tai")
else:
    print(f"Phan tu lon thu hai: {second}")
