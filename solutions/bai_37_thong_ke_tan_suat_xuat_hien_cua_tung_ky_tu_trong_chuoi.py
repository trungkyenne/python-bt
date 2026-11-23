# -*- coding: utf-8 -*-
r"""
Bài 37: Thống kê tần suất xuất hiện của từng ký tự trong chuỗi
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một chuỗi ký tự $S$. Hãy đếm số lần xuất hiện của từng ký tự trong chuỗi (phân biệt chữ hoa và chữ thường, không tính khoảng trắng). In kết quả theo thứ tự xuất hiện đầu tiên của mỗi ký tự.
"""

s = input("Nhập chuỗi: ")

freq = {}
for ch in s:
    if ch != " ":
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

for ch, count in freq.items():
    print(f"{ch}: {count}")
