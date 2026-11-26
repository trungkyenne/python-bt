# -*- coding: utf-8 -*-
"""
Bài 03: Tìm số nguyên tố lớn nhất và nhỏ nhất trong chuỗi.
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

if primes:
    print(f"Số nguyên tố lớn nhất: {max(primes)}")
    print(f"Số nguyên tố nhỏ nhất: {min(primes)}")
else:
    print("Không có số nguyên tố nào trong chuỗi.")
