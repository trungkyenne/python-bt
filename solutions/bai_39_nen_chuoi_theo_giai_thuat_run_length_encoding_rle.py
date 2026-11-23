# -*- coding: utf-8 -*-
r"""
Bài 39: Nén chuỗi theo giải thuật Run-Length Encoding (RLE)
Mức độ: Khó
Mục tiêu: Nén Run-Length (RLE) là phương pháp nén dữ liệu thay thế chuỗi các ký tự liên tiếp giống nhau bằng ký tự đó kèm theo số lần xuất hiện của nó. Ví dụ: 'AAABBBCC' nén thành 'A3B3C2', nếu ký tự đứng 1 mình (như 'A') thì ghi 'A1'. Viết chương trình nhập vào một chuỗi ký tự và in ra chuỗi sau khi nén RLE.
"""

s = input("Nhập chuỗi cần nén: ")

if not s:
    print("Nen RLE: ")
else:
    ket_qua = []
    current_char = s[0]
    count = 1
    
    for ch in s[1:]:
        if ch == current_char:
            count += 1
        else:
            ket_qua.append(f"{current_char}{count}")
            current_char = ch
            count = 1
            
    # Thêm đoạn cuối cùng
    ket_qua.append(f"{current_char}{count}")
    
    print(f"Nen RLE: {''.join(ket_qua)}")
