# -*- coding: utf-8 -*-
r"""
Bài 35: Đếm số từ trong câu và tìm từ dài nhất
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một câu văn bản gồm các từ cách nhau bởi một hoặc nhiều khoảng trắng. Hãy đếm tổng số từ trong câu và tìm ra từ có độ dài lớn nhất. Nếu có nhiều từ cùng độ dài lớn nhất, in ra từ xuất hiện đầu tiên.
"""

s = input("Nhập câu: ")

words = s.split()

if len(words) == 0:
    print("So luong tu: 0")
    print("Tu dai nhat: None")
else:
    tu_dai_nhat = words[0]
    for w in words[1:]:
        if len(w) > len(tu_dai_nhat):
            tu_dai_nhat = w
            
    print(f"So luong tu: {len(words)}")
    print(f"Tu dai nhat: {tu_dai_nhat} ({len(tu_dai_nhat)} ky tu)")
