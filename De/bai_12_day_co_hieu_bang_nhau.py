# -*- coding: utf-8 -*-
"""
Bài 12. Dãy có hiệu bằng nhau
Cho mảng số nguyên. Tìm đoạn liên tiếp dài nhất mà hiệu giữa hai phần tử
liền kề luôn bằng nhau (cấp số cộng liên tiếp).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if n < 2:
    print(f"Đoạn dài nhất: {nums}")
    print(f"Độ dài: {len(nums)}")
else:
    best_start = 0
    max_len = 2

    curr_start = 0
    curr_diff = nums[1] - nums[0]

    for i in range(2, n):
        diff = nums[i] - nums[i - 1]
        if diff == curr_diff:
            curr_len = i - curr_start + 1
            if curr_len > max_len:
                max_len = curr_len
                best_start = curr_start
        else:
            curr_start = i - 1
            curr_diff = diff

    best_sub = nums[best_start : best_start + max_len]
    print(f"Đoạn liên tiếp dài nhất có hiệu bằng nhau: {best_sub}")
    print(f"Độ dài: {max_len}")
    print(f"Hiệu chung: {best_sub[1] - best_sub[0]}")
