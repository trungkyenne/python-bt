# -*- coding: utf-8 -*-
"""
Bài 17: Tìm dãy số đối xứng tăng liên tiếp dài nhất.
(Số đối xứng / Palindrome là số đọc xuôi hay ngược đều giống nhau, n >= 0).
"""

def is_palindrome_number(n):
    if n < 0:
        return False
    s = str(n)
    return s == s[::-1]

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    if is_palindrome_number(x):
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

print(f"Dãy số đối xứng tăng liên tiếp dài nhất: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
