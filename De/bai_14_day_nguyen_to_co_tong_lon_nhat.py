# -*- coding: utf-8 -*-
"""
Bài 14. Dãy nguyên tố có tổng lớn nhất
Cho mảng số nguyên. Lọc các số nguyên tố, chia thành những đoạn tăng liên tiếp.
Tìm đoạn có tổng lớn nhất và xuất độ dài, tổng, các phần tử.
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
    segments = []
    curr_seg = [primes[0]]

    for i in range(1, len(primes)):
        if primes[i] > primes[i - 1]:
            curr_seg.append(primes[i])
        else:
            segments.append(curr_seg)
            curr_seg = [primes[i]]
    segments.append(curr_seg)

    best_seg = max(segments, key=sum)

    print(f"Đoạn nguyên tố tăng có tổng lớn nhất: {best_seg}")
    print(f"Độ dài: {len(best_seg)}")
    print(f"Tổng: {sum(best_seg)}")
