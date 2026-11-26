# -*- coding: utf-8 -*-
"""
Bài 07: Tìm hai số nguyên tố có khoảng cách nhỏ nhất trong chuỗi.
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

if len(primes) < 2:
    print("Không đủ 2 số nguyên tố để tìm khoảng cách.")
else:
    # Tìm cặp có hiệu tuyệt đối nhỏ nhất
    min_dist = float('inf')
    best_pairs = []
    
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            dist = abs(primes[i] - primes[j])
            if dist < min_dist:
                min_dist = dist
                best_pairs = [(primes[i], primes[j])]
            elif dist == min_dist:
                best_pairs.append((primes[i], primes[j]))
                
    print(f"Khoảng cách nhỏ nhất: {min_dist}")
    print(f"Các cặp số nguyên tố đạt khoảng cách nhỏ nhất: {best_pairs}")
