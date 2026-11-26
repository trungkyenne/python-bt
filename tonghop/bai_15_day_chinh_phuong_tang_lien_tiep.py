# -*- coding: utf-8 -*-
"""
Bài 15: Tìm dãy số chính phương tăng liên tiếp dài nhất.
"""

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(n**0.5)
    return r * r == n

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    if is_perfect_square(x):
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

print(f"Dãy số chính phương tăng liên tiếp dài nhất: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
