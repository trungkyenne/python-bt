# -*- coding: utf-8 -*-
"""
Bài 25. Tìm dãy con liên tiếp dài nhất có tổng các phần tử chia hết cho 5.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_start = -1
max_len = 0

# Duyệt tất cả các đoạn con liên tiếp
for i in range(len(nums)):
    curr_sum = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
        if curr_sum % 5 == 0:
            curr_len = j - i + 1
            if curr_len > max_len:
                max_len = curr_len
                best_start = i

if max_len > 0:
    best_sub = nums[best_start : best_start + max_len]
    print(f"Dãy con liên tiếp dài nhất có tổng chia hết cho 5: {best_sub}")
    print(f"Độ dài: {max_len}")
    print(f"Tổng: {sum(best_sub)} (chia hết cho 5)")
else:
    print("Không có dãy con nào có tổng chia hết cho 5.")
