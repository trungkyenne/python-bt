# -*- coding: utf-8 -*-
r"""
Bài 38: Mã hóa và giải mã chuỗi theo thuật toán Caesar Cipher
Mức độ: Khó
Mục tiêu: Mật mã Caesar là phương pháp mã hóa thay thế: mỗi chữ cái trong văn bản gốc được dịch chuyển đi $K$ vị trí trong bảng chữ cái (xoay vòng sau 'Z' về 'A'). Các ký tự không phải chữ cái được giữ nguyên. Viết chương trình nhập vào một chuỗi văn bản và số nguyên dịch chuyển $K$. Hãy in ra chuỗi sau khi mã hóa Caesar.
"""

s = input("Nhập chuỗi: ")
k = int(input("Nhập bước dịch K: "))

k = k % 26
ket_qua = []

for ch in s:
    if 'a' <= ch <= 'z':
        ma = chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
        ket_qua.append(ma)
    elif 'A' <= ch <= 'Z':
        ma = chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        ket_qua.append(ma)
    else:
        ket_qua.append(ch)

print(f"Ma hoa: {''.join(ket_qua)}")
