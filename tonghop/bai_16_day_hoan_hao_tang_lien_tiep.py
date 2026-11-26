# -*- coding: utf-8 -*-
"""
Bài 16: Tìm dãy số hoàn hảo tăng liên tiếp dài nhất.
(Số hoàn hảo là số nguyên dương có tổng các ước thực sự bằng chính nó, vd: 6, 28, 496, 8128,...)
"""

def is_perfect_number(n):
    if n <= 1:
        return False
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i * i != n:
                sum_div += n // i
    return sum_div == n

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

longest_sub = []
curr_sub = []

for x in nums:
    if is_perfect_number(x):
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

print(f"Dãy số hoàn hảo tăng liên tiếp dài nhất: {longest_sub}")
print(f"Độ dài: {len(longest_sub)}")
