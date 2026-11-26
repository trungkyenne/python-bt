# -*- coding: utf-8 -*-
"""
Bài 13: Tìm độ dài dãy số chẵn tăng liên tiếp dài nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

max_len = 0
curr_sub = []
longest_sub = []

for x in nums:
    if x % 2 == 0:
        if not curr_sub or x > curr_sub[-1]:
            curr_sub.append(x)
        else:
            if len(curr_sub) > max_len:
                max_len = len(curr_sub)
                longest_sub = curr_sub
            curr_sub = [x]
    else:
        if len(curr_sub) > max_len:
            max_len = len(curr_sub)
            longest_sub = curr_sub
        curr_sub = []

if len(curr_sub) > max_len:
    max_len = len(curr_sub)
    longest_sub = curr_sub

print(f"Dãy số chẵn tăng liên tiếp dài nhất: {longest_sub}")
print(f"Độ dài: {max_len}")
