# -*- coding: utf-8 -*-
r"""
Bài 27: Kiểm tra số nguyên tố
Mức độ: Trung bình
Mục tiêu: Số nguyên tố là số nguyên lớn hơn 1 và chỉ có đúng 2 ước nguyên dương là 1 và chính nó. Viết chương trình nhập vào số nguyên $N$. Hãy kiểm tra xem $N$ có phải là số nguyên tố hay không. Tối ưu thuật toán kiểm tra ước đến căn bậc hai của $N$.
"""

n = int(input("Nhập số nguyên N: "))

if n < 2:
    is_prime = False
elif n == 2:
    is_prime = True
elif n % 2 == 0:
    is_prime = False
else:
    is_prime = True
    i = 3
    while i * i <= n:
        if n % i == 0:
            is_prime = False
            break
        i += 2

if is_prime:
    print("So nguyen to")
else:
    print("Khong phai so nguyen to")
