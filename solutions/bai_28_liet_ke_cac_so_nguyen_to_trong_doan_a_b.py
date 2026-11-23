# -*- coding: utf-8 -*-
r"""
Bài 28: Liệt kê các số nguyên tố trong đoạn [A, B]
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào hai số nguyên dương $A$ và $B$ ($A \le B$). Hãy liệt kê tất cả các số nguyên tố nằm trong đoạn $[A, B]$ trên cùng một dòng, cách nhau bởi khoảng trắng. Đếm tổng số lượng số nguyên tố tìm được.
"""

a, b = map(int, input("Nhập đoạn A B: ").split())

primes = []

for num in range(a, b + 1):
    if num >= 2:
        is_p = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_p = False
                break
        if is_p:
            primes.append(str(num))

print(" ".join(primes))
print(f"Tong so luong: {len(primes)}")
