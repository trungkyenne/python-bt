# -*- coding: utf-8 -*-
"""
Bài 01: Nhập một chuỗi số nguyên, tách thành các số và đếm số lượng số nguyên tố.
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
primes = [x for x in nums if is_prime(x)]

print(f"Các số đã tách: {nums}")
print(f"Các số nguyên tố: {primes}")
print(f"Số lượng số nguyên tố: {len(primes)}")
