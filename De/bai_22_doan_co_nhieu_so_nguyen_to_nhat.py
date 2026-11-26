# -*- coding: utf-8 -*-
"""
Bài 22. Tìm đoạn có số lượng số nguyên tố nhiều nhất trong mảng.
Cho mảng số nguyên. Tìm đoạn con liên tiếp gồm toàn các số nguyên tố có độ dài lớn nhất
(hoặc đoạn con liên tiếp có mật độ/số lượng số nguyên tố nhiều nhất).
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

# Tìm đoạn con liên tiếp gồm toàn số nguyên tố có nhiều phần tử nhất
prime_segments = []
curr_seg = []

for x in nums:
    if is_prime(x):
        curr_seg.append(x)
    else:
        if curr_seg:
            prime_segments.append(curr_seg)
            curr_seg = []
if curr_seg:
    prime_segments.append(curr_seg)

if not prime_segments:
    print("Mảng không chứa số nguyên tố nào.")
else:
    best_seg = max(prime_segments, key=len)
    print(f"Đoạn liên tiếp gồm toàn số nguyên tố nhiều nhất: {best_seg}")
    print(f"Số lượng số nguyên tố: {len(best_seg)}")
