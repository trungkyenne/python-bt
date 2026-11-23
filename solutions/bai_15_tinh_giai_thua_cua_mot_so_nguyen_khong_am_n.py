# -*- coding: utf-8 -*-
r"""
Bài 15: Tính giai thừa của một số nguyên không âm N!
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào số nguyên không âm $N$. Hãy tính và in ra giá trị giai thừa $N! = 1 \times 2 \times \dots \times N$. Quy ước: $0! = 1$.
"""

n = int(input("Nhập số nguyên không âm N: "))

giai_thua = 1
for i in range(1, n + 1):
    giai_thua *= i

print(f"{n}! = {giai_thua}")
