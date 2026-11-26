# -*- coding: utf-8 -*-
"""
Bài 04: Tính tổng các số nguyên tố trong chuỗi.
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

total = sum(primes)
print(f"Tổng các số nguyên tố: {total}")
