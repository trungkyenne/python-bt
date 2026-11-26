# -*- coding: utf-8 -*-
"""
Bài 27: Lọc số nguyên tố, sau đó tìm dãy con có tổng lớn nhất.
(Vì các số nguyên tố đều dương >= 2, dãy con liên tiếp có tổng lớn nhất của danh sách các số nguyên tố chính là toàn bộ danh sách các số nguyên tố đã lọc).
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
    # Do các số nguyên tố đều > 0, tổng dãy con liên tiếp lớn nhất chính là toàn bộ dãy primes
    print(f"Các số nguyên tố đã lọc: {primes}")
    print(f"Dãy con có tổng lớn nhất: {primes}")
    print(f"Tổng lớn nhất: {sum(primes)}")
