# -*- coding: utf-8 -*-
r"""
Bài 54: Xây dựng hàm đệ quy tính lũy thừa nhanh (Binary Exponentiation)
Mức độ: Khó
Mục tiêu: Hãy xây dựng một hàm đệ quy `power(a, b)` để tính lũy thừa $a^b$ ($b \ge 0$) theo giải thuật lũy thừa nhanh (Binary Exponentiation) với độ phức tạp $O(\log b)$:\n- Nếu $b = 0$: trả về 1.\n- Nếu $b$ chẵn: $a^b = (a^{b/2})^2$.\n- Nếu $b$ lẻ: $a^b = a \times a^{b-1}$.
"""

def power(a, b):
    # Điểm dừng đệ quy
    if b == 0:
        return 1.0
    
    # Bước đệ quy
    half = power(a, b // 2)
    if b % 2 == 0:
        return half * half
    else:
        return a * half * half

# Chương trình chính
a, b = input("Nhập a và b: ").split()
a = float(a)
b = int(b)

res = power(a, b)
print(f"Gia tri: {res:.4f}")
