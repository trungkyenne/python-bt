# -*- coding: utf-8 -*-
r"""
Bài 33: Đếm số ký tự nguyên âm, phụ âm và ký tự số trong chuỗi
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một chuỗi ký tự $S$. Hãy đếm và in ra số lượng chữ cái nguyên âm (tiếng Anh: a, e, i, o, u không phân biệt hoa thường), số lượng chữ cái phụ âm và số lượng chữ số (0-9) xuất hiện trong chuỗi.
"""

s = input("Nhập chuỗi: ")

nguyen_am = 0
phu_am = 0
chu_so = 0

vowels = "aeiou"

for ch in s:
    if ch.isdigit():
        chu_so += 1
    elif ch.isalpha():
        if ch.lower() in vowels:
            nguyen_am += 1
        else:
            phu_am += 1

print(f"Nguyen am: {nguyen_am}")
print(f"Phu am: {phu_am}")
print(f"Chu so: {chu_so}")
