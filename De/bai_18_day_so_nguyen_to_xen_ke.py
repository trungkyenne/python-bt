# -*- coding: utf-8 -*-
"""
Bài 18. Dãy số nguyên tố xen kẽ
Cho mảng số nguyên. Lọc các số nguyên tố. Tìm đoạn dài nhất mà các phần tử
liên tiếp có giá trị luân phiên tăng và giảm (zigzag / alternating).
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
elif len(primes) < 3:
    print(f"Đoạn xen kẽ dài nhất: {primes}")
    print(f"Độ dài: {len(primes)}")
else:
    best_sub = primes[:1]
    # Duyệt tìm đoạn luân phiên dài nhất
    for i in range(len(primes)):
        curr = [primes[i]]
        for j in range(i + 1, len(primes)):
            if len(curr) == 1:
                if primes[j] != curr[-1]:
                    curr.append(primes[j])
                else:
                    break
            else:
                prev_diff = curr[-1] - curr[-2]
                curr_diff = primes[j] - curr[-1]
                # Xen kẽ tăng giảm: tích hai hiệu liền kề âm
                if prev_diff * curr_diff < 0:
                    curr.append(primes[j])
                else:
                    break
        if len(curr) > len(best_sub):
            best_sub = curr

    print(f"Đoạn số nguyên tố luân phiên tăng giảm dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
