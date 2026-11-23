# -*- coding: utf-8 -*-
r"""
Bài 57: Thống kê từ vựng và tần suất xuất hiện trong văn bản
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào một đoạn văn bản (gồm nhiều câu, có thể chứa dấu chấm, phẩy, chấm than, hỏi chấm). Hãy:\n1. Tách đoạn văn thành các từ (chuyển toàn bộ về chữ thường, loại bỏ các dấu câu: `, . ! ? ; :`).\n2. Đếm tần suất xuất hiện của từng từ.\n3. In danh sách các từ và số lần xuất hiện theo thứ tự giảm dần của tần suất. Nếu hai từ có cùng tần suất, sắp xếp theo thứ tự bảng chữ cái alphabet tăng dần.
"""

van_ban = input("Nhập văn bản: ")

dau_cau = ",.!?;:()\"'"
for ch in dau_cau:
    van_ban = van_ban.replace(ch, " ")

words = van_ban.lower().split()
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1

# Sắp xếp theo: tần suất giảm (-val), từ tăng (key)
sorted_words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))

for w, count in sorted_words:
    print(f"{w}: {count}")
