# -*- coding: utf-8 -*-
r"""
Bài 30: Kiểm tra số đối xứng (Số Palindrome)
Mức độ: Trung bình
Mục tiêu: Một số nguyên dương được gọi là số đối xứng (Palindrome) nếu đọc từ trái sang phải hay từ phải sang trái đều thu được số như nhau (ví dụ: 121, 12321, 7). Hãy viết chương trình kiểm tra xem một số nguyên dương $N$ có phải là số đối xứng hay không bằng thuật toán số học.
"""

n = int(input("Nhập số nguyên dương N: "))

temp = n
rev = 0

while temp > 0:
    rev = rev * 10 + (temp % 10)
    temp //= 10

if rev == n:
    print("So doi xung")
else:
    print("Khong phai so doi xung")
