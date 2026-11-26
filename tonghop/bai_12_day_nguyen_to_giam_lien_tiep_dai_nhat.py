# -*- coding: utf-8 -*-
"""
Bài 12: Tìm dãy số nguyên tố giảm liên tiếp dài nhất.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    if is_prime(x):
        if not curr_sub or x < curr_sub[-1]:
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

if longest_sub:
    print(f"Dãy số nguyên tố giảm liên tiếp dài nhất: {longest_sub}")
    print(f"Độ dài: {len(longest_sub)}")
else:
    print("Không tìm thấy dãy số nguyên tố giảm liên tiếp.")
