# -*- coding: utf-8 -*-
"""
Bài 23. Tìm đoạn liên tiếp có tổng bằng K.
Cho mảng số nguyên và số K. Tìm đoạn con liên tiếp có tổng các phần tử đúng bằng K.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
k_target = int(input("Nhập giá trị K: "))

found = False
# Duyệt tìm đoạn liên tiếp có tổng bằng K
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
        if curr_sum == k_target:
            seg = nums[i : j + 1]
            print(f"Tìm thấy đoạn từ chỉ số {i} đến {j}: {seg}")
            print(f"Tổng: {curr_sum} = {k_target}")
            found = True
            break
    if found:
        break

if not found:
    print(f"Không có đoạn liên tiếp nào có tổng bằng {k_target}.")
