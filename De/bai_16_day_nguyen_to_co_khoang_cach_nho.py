# -*- coding: utf-8 -*-
"""
Bài 16. Dãy nguyên tố có khoảng cách nhỏ
Cho mảng số nguyên. Lọc số nguyên tố. Tìm đoạn liên tiếp dài nhất
sao cho hiệu giữa hai phần tử liền kề không vượt quá 4 và luôn tăng dần.
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
    print("Không có số nguyên tố nào.")
else:
    best_sub = [primes[0]]
    curr_sub = [primes[0]]

    for i in range(1, len(primes)):
        diff = primes[i] - primes[i - 1]
        if 0 < diff <= 4:
            curr_sub.append(primes[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [primes[i]]

    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Đoạn nguyên tố tăng dần có khoảng cách <= 4 dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
