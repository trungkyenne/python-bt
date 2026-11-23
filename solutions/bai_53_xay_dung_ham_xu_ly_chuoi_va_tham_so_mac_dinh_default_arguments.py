# -*- coding: utf-8 -*-
r"""
Bài 53: Xây dựng hàm xử lý chuỗi và tham số mặc định (Default Arguments)
Mức độ: Khó
Mục tiêu: Hãy xây dựng một hàm `format_text(text, max_len=20, fill_char='.')` thực hiện nhiệm vụ định dạng chuỗi: Nếu chuỗi `text` có độ dài nhỏ hơn `max_len`, hãy bù các ký tự `fill_char` vào bên phải cho đến khi đạt độ dài `max_len`. Nếu chuỗi dài hơn `max_len`, cắt ngắn chuỗi lấy `max_len - 3` ký tự đầu và nối thêm '...' vào cuối. Viết chương trình minh họa gọi hàm với các bộ tham số khác nhau.
"""

def format_text(text, max_len=20, fill_char='.'):
    if len(text) < max_len:
        return text + fill_char * (max_len - len(text))
    elif len(text) > max_len:
        if max_len >= 3:
            return text[:max_len - 3] + "..."
        return text[:max_len]
    return text

# Chương trình chính
s = input("Nhập chuỗi: ")
ml = int(input("Nhập max_len: "))
fc = input("Nhập fill_char: ")

print(f"Ket qua dinh dang: {format_text(s, ml, fc)}")
