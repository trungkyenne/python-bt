# -*- coding: utf-8 -*-
r"""
Bài 31: Tìm số Fibonacci thứ N và liệt kê dãy
Mức độ: Khó
Mục tiêu: Dãy số Fibonacci được định nghĩa đệ quy như sau: $F_0 = 0, F_1 = 1$, và $F_n = F_{n-1} + F_{n-2}$ với mọi $n \ge 2$. Hãy viết chương trình nhập vào số nguyên dương $N$ ($N \le 50$). In ra danh sách $N$ số Fibonacci đầu tiên ($F_0$ đến $F_{N-1}$) và giá trị của số thứ $N$ ($F_{N-1}$).
"""

n = int(input("Nhập số lượng số Fibonacci N: "))

fib = []
if n >= 1:
    fib.append(0)
if n >= 2:
    fib.append(1)

for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])

print(" ".join(map(str, fib)))
print(f"Gia tri thu N: {fib[-1]}")
