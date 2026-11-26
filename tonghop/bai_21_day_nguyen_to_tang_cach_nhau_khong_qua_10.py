# -*- coding: utf-8 -*-
"""
Bài 21: Tìm dãy số nguyên tố tăng dài nhất có các phần tử liên tiếp cách nhau không quá 10.
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
        if not curr_sub:
            curr_sub.append(x)
        elif x > curr_sub[-1] and (x - curr_sub[-1]) <= 10:
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

print(f"Dãy số nguyên tố tăng dài nhất có phần tử cách nhau <= 10: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
