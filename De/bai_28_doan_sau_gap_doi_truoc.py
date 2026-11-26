# -*- coding: utf-8 -*-
"""
Bài 28. Tìm đoạn liên tiếp dài nhất mà mỗi phần tử sau gấp đôi phần tử trước.
(Tức nums[i] == 2 * nums[i - 1]).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Mảng rỗng.")
else:
    best_sub = [nums[0]]
    curr_sub = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == 2 * nums[i - 1]:
            curr_sub.append(nums[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [nums[i]]

    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Đoạn liên tiếp dài nhất có phần tử sau gấp đôi phần tử trước: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
