# -*- coding: utf-8 -*-
"""
Bài 02: Lọc tất cả số nguyên tố trong chuỗi và xuất thành chuỗi mới.
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
res_str = " ".join(str(x) for x in primes)

print(f"Chuỗi các số nguyên tố: {res_str}")
