# -*- coding: utf-8 -*-
"""
Bài 31: Tìm dãy số nguyên tố tăng dài nhất, thay thế các phần tử còn lại bằng 0.
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

best_start = -1
best_len = 0

curr_start = -1
curr_len = 0

for i, x in enumerate(nums):
    if is_prime(x):
        if curr_len == 0:
            curr_start = i
            curr_len = 1
        elif x > nums[i - 1]:
            curr_len += 1
        else:
            if curr_len > best_len:
                best_len = curr_len
                best_start = curr_start
            curr_start = i
            curr_len = 1
    else:
        if curr_len > best_len:
            best_len = curr_len
            best_start = curr_start
        curr_start = -1
        curr_len = 0

if curr_len > best_len:
    best_len = curr_len
    best_start = curr_start

if best_len > 0:
    res = [0] * len(nums)
    for i in range(best_start, best_start + best_len):
        res[i] = nums[i]
    print(f"Dãy số nguyên tố tăng dài nhất: {nums[best_start : best_start + best_len]}")
    print(f"Kết quả sau khi thay các phần tử còn lại bằng 0: {' '.join(map(str, res))}")
else:
    print("Không có dãy số nguyên tố nào.")
