# -*- coding: utf-8 -*-
"""
Bài 05: Đếm số lượng số nguyên tố liên tiếp xuất hiện trong chuỗi ban đầu.
(Đếm số lượng khối/đoạn các số nguyên tố xuất hiện liên tiếp nhau,
 hoặc liệt kê số lượng phần tử trong từng đoạn liên tiếp).
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

# Tìm các đoạn liên tiếp gồm các số nguyên tố
prime_segments = []
current_segment = []

for x in nums:
    if is_prime(x):
        current_segment.append(x)
    else:
        if current_segment:
            prime_segments.append(current_segment)
            current_segment = []
if current_segment:
    prime_segments.append(current_segment)

print(f"Các đoạn số nguyên tố liên tiếp: {prime_segments}")
print(f"Số lượng đoạn số nguyên tố liên tiếp: {len(prime_segments)}")
for idx, seg in enumerate(prime_segments, 1):
    print(f"  Đoạn {idx}: {seg} (độ dài: {len(seg)})")
