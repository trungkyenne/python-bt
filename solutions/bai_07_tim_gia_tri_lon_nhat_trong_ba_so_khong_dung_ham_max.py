# -*- coding: utf-8 -*-
r"""
Bài 07: Tìm giá trị lớn nhất trong ba số không dùng hàm max()
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào 3 số thực $a, b, c$. Hãy tìm và in ra giá trị lớn nhất trong 3 số đó. Yêu cầu: Không sử dụng hàm có sẵn `max()`, chỉ sử dụng cấu trúc rẽ nhánh `if-elif-else`.
"""

a, b, c = map(float, input("Nhập 3 số a b c: ").split())

max_val = a
if b > max_val:
    max_val = b
if c > max_val:
    max_val = c

print(f"Gia tri lon nhat: {max_val:.2f}")
