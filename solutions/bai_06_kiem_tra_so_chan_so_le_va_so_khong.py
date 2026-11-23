# -*- coding: utf-8 -*-
r"""
Bài 06: Kiểm tra số chẵn, số lẻ và số không
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một số nguyên $n$. Hãy kiểm tra và in ra thông báo xem $n$ là số không ('So khong'), số chẵn ('So chan') hay số lẻ ('So le'). Đồng thời cho biết số đó là số dương ('duong') hay số âm ('am') nếu khác 0.
"""

n = int(input("Nhập số nguyên n: "))

if n == 0:
    print("So khong")
else:
    loai_so = "So chan" if n % 2 == 0 else "So le"
    dau = "duong" if n > 0 else "am"
    print(f"{loai_so} {dau}")
