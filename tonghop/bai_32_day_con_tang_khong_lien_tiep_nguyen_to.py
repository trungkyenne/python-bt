# -*- coding: utf-8 -*-
"""
Bài 32: Tìm dãy con tăng dài nhất không nhất thiết phải liên tiếp (LIS), chỉ xét các số nguyên tố.
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

if not primes:
    print("Không có số nguyên tố nào trong chuỗi.")
else:
    n = len(primes)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if primes[j] < primes[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
                
    max_len = max(dp)
    last_idx = dp.index(max_len)
    
    # Truy vết dãy con
    lis = []
    curr = last_idx
    while curr != -1:
        lis.append(primes[curr])
        curr = parent[curr]
    lis.reverse()
    
    print(f"Các số nguyên tố được xét: {primes}")
    print(f"Dãy con tăng dài nhất (không nhất thiết liên tiếp): {lis}")
    print(f"Độ dài: {max_len}")
