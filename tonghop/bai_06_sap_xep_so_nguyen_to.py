# -*- coding: utf-8 -*-
"""
Bài 06: Sắp xếp các số nguyên tố tăng dần, giữ nguyên các số không nguyên tố.
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

# Lọc và sắp xếp các số nguyên tố
primes = sorted([x for x in nums if is_prime(x)])

# Điền lại vào danh sách kết quả
result = []
prime_idx = 0
for x in nums:
    if is_prime(x):
        result.append(primes[prime_idx])
        prime_idx += 1
    else:
        result.append(x)

print(f"Chuỗi sau khi sắp xếp số nguyên tố: {' '.join(map(str, result))}")
