# -*- coding: utf-8 -*-
r"""
Bài 47: Sắp xếp danh sách bằng thuật toán chọn (Selection Sort)
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên. Hãy cài đặt thuật toán sắp xếp chọn (Selection Sort) để sắp xếp danh sách theo thứ tự giảm dần mà không dùng các hàm sắp xếp có sẵn.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))
n = len(nums)

for i in range(n - 1):
    max_idx = i
    for j in range(i + 1, n):
        if nums[j] > nums[max_idx]:
            max_idx = j
    if max_idx != i:
        nums[i], nums[max_idx] = nums[max_idx], nums[i]

print(" ".join(map(str, nums)))
