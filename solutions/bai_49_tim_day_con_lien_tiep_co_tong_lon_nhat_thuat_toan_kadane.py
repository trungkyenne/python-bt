# -*- coding: utf-8 -*-
r"""
Bài 49: Tìm dãy con liên tiếp có tổng lớn nhất (Thuật toán Kadane)
Mức độ: Khó
Mục tiêu: Cho một danh sách gồm các số nguyên (có thể có cả số âm). Hãy tìm một dãy con liên tiếp không rỗng có tổng các phần tử là lớn nhất và in ra giá trị tổng lớn nhất đó.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))

current_max = nums[0]
max_so_far = nums[0]

for x in nums[1:]:
    # Quyết định bắt đầu chuỗi mới tại x hay cộng nối tiếp
    if current_max + x > x:
        current_max = current_max + x
    else:
        current_max = x
        
    if current_max > max_so_far:
        max_so_far = current_max

print(f"Tong lon nhat: {max_so_far}")
