# -*- coding: utf-8 -*-
r"""
Bài 10: Giải và biện luận phương trình bậc hai $ax^2 + bx + c = 0$
Mức độ: Trung bình
Mục tiêu: Viết chương trình giải và biện luận phương trình bậc hai: $ax^2 + bx + c = 0$. In ra nghiệm của phương trình tùy theo từng trường hợp (vô nghiệm, vô số nghiệm, nghiệm duy nhất, nghiệm kép, hai nghiệm phân biệt).
"""

a, b, c = map(float, input("Nhập hệ số a b c: ").split())

if a == 0:
    if b == 0:
        if c == 0:
            print("Vo so nghiem")
        else:
            print("Vo nghiem")
    else:
        x = -c / b
        print(f"Mot nghiem x = {x:.2f}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        x = -b / (2*a)
        print(f"Nghiem kep x = {x:.2f}")
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        if x1 > x2:
            x1, x2 = x2, x1
        print(f"Hai nghiem phan biet x1 = {x1:.2f}, x2 = {x2:.2f}")
