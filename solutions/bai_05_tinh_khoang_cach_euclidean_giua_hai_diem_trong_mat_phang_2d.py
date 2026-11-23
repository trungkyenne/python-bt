# -*- coding: utf-8 -*-
r"""
Bài 05: Tính khoảng cách Euclidean giữa hai điểm trong mặt phẳng 2D
Mức độ: Khó
Mục tiêu: Trong hệ tọa độ Descartes Oxy, cho hai điểm $A(x_1, y_1)$ và $B(x_2, y_2)$. Hãy viết chương trình nhập tọa độ của hai điểm trên từ bàn phím, tính và in ra khoảng cách $d(A, B)$ giữa hai điểm. Không dùng thư viện `math`.
"""

# Nhập tọa độ hai điểm A và B
x1, y1 = map(float, input("Nhập x1 y1: ").split())
x2, y2 = map(float, input("Nhập x2 y2: ").split())

# Tính khoảng cách không dùng thư viện math
khoang_cach = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# In kết quả
print(f"Khoang cach: {khoang_cach:.4f}")
