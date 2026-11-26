# -*- coding: utf-8 -*-
"""
Bài 24: Tìm dãy số tăng dài nhất mà các phần tử đều có chữ số cuối giống nhau.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    last_digit = abs(x) % 10
    if not curr_sub:
        curr_sub.append(x)
    elif x > curr_sub[-1] and abs(curr_sub[-1]) % 10 == last_digit:
        curr_sub.append(x)
    else:
        if len(curr_sub) > len(longest_sub):
            longest_sub = curr_sub
        curr_sub = [x]

if len(curr_sub) > len(longest_sub):
    longest_sub = curr_sub

print(f"Dãy số tăng dài nhất có chữ số cuối giống nhau: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
