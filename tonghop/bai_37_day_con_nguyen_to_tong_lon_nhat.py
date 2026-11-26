# -*- coding: utf-8 -*-
"""
Bài 37: Tìm dãy con có tổng lớn nhất mà tất cả phần tử đều là số nguyên tố.
(Xét dãy con liên tiếp trong chuỗi ban đầu gồm toàn số nguyên tố có tổng lớn nhất;
hoặc nếu xét toàn bộ chuỗi số nguyên tố đã lọc).
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

# Cách 1: Dãy con liên tiếp trong chuỗi ban đầu toàn là số nguyên tố
best_sub = []
curr_sub = []

for x in nums:
    if is_prime(x):
        curr_sub.append(x)
    else:
        if sum(curr_sub) > sum(best_sub):
            best_sub = curr_sub
        curr_sub = []

if sum(curr_sub) > sum(best_sub):
    best_sub = curr_sub

if best_sub:
    print(f"Dãy con liên tiếp gồm toàn số nguyên tố có tổng lớn nhất: {best_sub}")
    print(f"Tổng: {sum(best_sub)}")
else:
    print("Không có số nguyên tố nào trong chuỗi.")
