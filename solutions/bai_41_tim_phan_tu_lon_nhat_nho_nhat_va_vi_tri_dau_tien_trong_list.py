# -*- coding: utf-8 -*-
r"""
Bài 41: Tìm phần tử lớn nhất, nhỏ nhất và vị trí đầu tiên trong List
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào danh sách các số thực. Hãy tìm giá trị lớn nhất (Max) và giá trị nhỏ nhất (Min) cùng chỉ số (index bắt đầu từ 0) xuất hiện đầu tiên của chúng trong danh sách mà không dùng hàm `max()` và `min()` có sẵn.
"""

nums = list(map(float, input("Nhập danh sách số thực: ").split()))

max_val = nums[0]
max_idx = 0
min_val = nums[0]
min_idx = 0

for i in range(1, len(nums)):
    if nums[i] > max_val:
        max_val = nums[i]
        max_idx = i
    if nums[i] < min_val:
        min_val = nums[i]
        min_idx = i

print(f"Max: {max_val:.2f} tai vi tri {max_idx}")
print(f"Min: {min_val:.2f} tai vi tri {min_idx}")
