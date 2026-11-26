# -*- coding: utf-8 -*-
"""
Bài 1. Dãy số nguyên tố tăng dài nhất
Cho mảng gồm n số nguyên. Lọc ra các số nguyên tố theo đúng thứ tự xuất hiện.
Tìm dãy con liên tiếp có các phần tử tăng nghiêm ngặt dài nhất trong mảng đã lọc.
Xuất độ dài và các phần tử của dãy.
"""

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

primes = [x for x in nums if is_prime(x)]
print(f"Các số nguyên tố đã lọc: {primes}")

if not primes:
    print("Không có số nguyên tố nào trong mảng.")
else:
    best_sub = [primes[0]]
    curr_sub = [primes[0]]
    for i in range(1, len(primes)):
        if primes[i] > primes[i - 1]:
            curr_sub.append(primes[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [primes[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Độ dài: {len(best_sub)}")
    print(f"Dãy con tăng nghiêm ngặt dài nhất: {best_sub}")
