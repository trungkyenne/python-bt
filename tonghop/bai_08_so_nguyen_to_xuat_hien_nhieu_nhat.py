# -*- coding: utf-8 -*-
"""
Bài 08: Tìm số nguyên tố xuất hiện nhiều lần nhất.
"""
from collections import Counter

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
primes = [x for x in nums if is_prime(x)]

if not primes:
    print("Không có số nguyên tố nào trong chuỗi.")
else:
    counts = Counter(primes)
    max_count = max(counts.values())
    most_frequent = [val for val, count in counts.items() if count == max_count]
    
    print(f"Số lần xuất hiện nhiều nhất: {max_count}")
    print(f"Các số nguyên tố xuất hiện nhiều nhất: {most_frequent}")
