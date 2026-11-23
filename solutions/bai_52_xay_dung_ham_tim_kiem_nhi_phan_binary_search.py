# -*- coding: utf-8 -*-
r"""
Bài 52: Xây dựng hàm tìm kiếm nhị phân (Binary Search)
Mức độ: Trung bình
Mục tiêu: Thuật toán tìm kiếm nhị phân tìm kiếm một phần tử trong một danh sách đã được sắp xếp tăng dần bằng cách liên tục chia đôi không gian tìm kiếm. Hãy viết hàm `binary_search(arr, target)` nhận vào một danh sách đã sắp xếp `arr` và giá trị cần tìm `target`. Hàm trả về chỉ số của `target` trong danh sách nếu tìm thấy, hoặc trả về -1 nếu không tìm thấy.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Chương trình chính
arr = list(map(int, input("Nhập danh sách đã sắp xếp: ").split()))
target = int(input("Nhập số cần tìm: "))

idx = binary_search(arr, target)
if idx != -1:
    print(f"Vi tri tim thay: {idx}")
else:
    print("Khong tim thay")
