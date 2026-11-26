# -*- coding: utf-8 -*-
"""
Bài 20. Dãy thỏa mãn nhiều điều kiện
Cho mảng số nguyên. Lọc các số vừa là số nguyên tố, vừa nhỏ hơn 100.
Tìm đoạn tăng liên tiếp dài nhất. Nếu có nhiều đoạn cùng độ dài, chọn đoạn có tổng lớn nhất.
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

primes_under_100 = [x for x in nums if is_prime(x) and x < 100]
print(f"Các số nguyên tố < 100 đã lọc: {primes_under_100}")

if not primes_under_100:
    print("Không có phần tử nào thỏa mãn điều kiện.")
else:
    segments = []
    curr_seg = [primes_under_100[0]]

    for i in range(1, len(primes_under_100)):
        if primes_under_100[i] > primes_under_100[i - 1]:
            curr_seg.append(primes_under_100[i])
        else:
            segments.append(curr_seg)
            curr_seg = [primes_under_100[i]]
    segments.append(curr_seg)

    # Chọn đoạn có độ dài lớn nhất, nếu trùng độ dài thì chọn đoạn có tổng lớn nhất
    best_seg = max(segments, key=lambda seg: (len(seg), sum(seg)))

    print(f"Đoạn nguyên tố (< 100) tăng dài nhất (ưu tiên tổng lớn nhất): {best_seg}")
    print(f"Độ dài: {len(best_seg)}")
    print(f"Tổng: {sum(best_seg)}")
