# -*- coding: utf-8 -*-
"""
Bài 14: Tìm dãy số lẻ tăng liên tiếp dài nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    if x % 2 != 0:
        if not curr_sub or x > curr_sub[-1]:
            curr_sub.append(x)
        else:
            if len(curr_sub) > len(longest_sub):
                longest_sub = curr_sub
            curr_sub = [x]
    else:
        if len(curr_sub) > len(longest_sub):
            longest_sub = curr_sub
        curr_sub = []

if len(curr_sub) > len(longest_sub):
    longest_sub = curr_sub

print(f"Dãy số lẻ tăng liên tiếp dài nhất: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
