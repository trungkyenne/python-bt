# -*- coding: utf-8 -*-
r"""
Bài 48: Trộn hai danh sách đã sắp xếp thành một danh sách sắp xếp (Merge Step)
Mức độ: Khó
Mục tiêu: Cho hai danh sách số nguyên $A$ và $B$ đã được sắp xếp theo thứ tự tăng dần. Hãy viết chương trình trộn hai danh sách này thành một danh sách mới $C$ duy nhất cũng có thứ tự tăng dần với độ phức tạp $O(len(A) + len(B))$. Không được gộp hai danh sách rồi gọi hàm sắp xếp lại.
"""

a = list(map(int, input("Nhập danh sách A: ").split()))
b = list(map(int, input("Nhập danh sách B: ").split()))

c = []
i = 0
j = 0

while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

# Thêm các phần tử còn lại
while i < len(a):
    c.append(a[i])
    i += 1

while j < len(b):
    c.append(b[j])
    j += 1

print(" ".join(map(str, c)))
