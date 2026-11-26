# -*- coding: utf-8 -*-
"""
Bài 29: Nhập chuỗi số, lọc số nguyên tố, sắp xếp tăng dần, tìm số nguyên tố lớn thứ hai.
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
primes = sorted([x for x in nums if is_prime(x)])

print(f"Các số nguyên tố sau khi sắp xếp tăng dần: {primes}")

# Lấy các giá trị nguyên tố phân biệt để tìm số lớn thứ hai
unique_primes = sorted(list(set(primes)))
if len(unique_primes) < 2:
    print("Không đủ số nguyên tố phân biệt để tìm số lớn thứ hai.")
else:
    print(f"Số nguyên tố lớn thứ hai: {unique_primes[-2]}")
