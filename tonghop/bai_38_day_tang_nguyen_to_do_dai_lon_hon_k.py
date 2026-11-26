# -*- coding: utf-8 -*-
"""
Bài 38: Tìm tất cả các dãy con tăng có độ dài lớn hơn K và các phần tử đều là số nguyên tố.
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
k = int(input("Nhập K: "))

results = []
n = len(nums)

# Tìm các dãy con liên tiếp tăng gồm toàn số nguyên tố có độ dài > K
for i in range(n):
    if is_prime(nums[i]):
        curr = [nums[i]]
        for j in range(i + 1, n):
            if is_prime(nums[j]) and nums[j] > nums[j - 1]:
                curr.append(nums[j])
            else:
                break
        if len(curr) > k and curr not in results:
            results.append(curr)

print(f"Các dãy con liên tiếp tăng có độ dài > {k} và toàn số nguyên tố:")
if results:
    for idx, r in enumerate(results, 1):
        print(f"  {idx}. {r} (độ dài: {len(r)})")
else:
    print(f"Không có dãy nào có độ dài > {k}.")
