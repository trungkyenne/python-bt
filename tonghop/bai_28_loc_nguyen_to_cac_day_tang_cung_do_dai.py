# -*- coding: utf-8 -*-
"""
Bài 28: Lọc số nguyên tố, tìm dãy tăng dài nhất và xuất tất cả các dãy có cùng độ dài lớn nhất.
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
    # Tìm tất cả các dãy con tăng liên tiếp trong chuỗi số nguyên tố đã lọc
    all_runs = []
    curr = [primes[0]]
    for i in range(1, len(primes)):
        if primes[i] > primes[i - 1]:
            curr.append(primes[i])
        else:
            all_runs.append(curr)
            curr = [primes[i]]
    all_runs.append(curr)

    max_len = max(len(r) for r in all_runs)
    longest_runs = [r for r in all_runs if len(r) == max_len]

    print(f"Các số nguyên tố đã lọc: {primes}")
    print(f"Độ dài lớn nhất: {max_len}")
    print("Tất cả các dãy tăng có cùng độ dài lớn nhất:")
    for idx, r in enumerate(longest_runs, 1):
        print(f"  Dãy {idx}: {r}")
