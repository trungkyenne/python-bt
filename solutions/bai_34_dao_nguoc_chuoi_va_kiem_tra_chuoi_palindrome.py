# -*- coding: utf-8 -*-
r"""
Bài 34: Đảo ngược chuỗi và kiểm tra chuỗi Palindrome
Mức độ: Dễ
Mục tiêu: Viết chương trình nhập vào một chuỗi ký tự $S$. Hãy in ra chuỗi đảo ngược của nó, sau đó kiểm tra xem chuỗi có phải là chuỗi đối xứng (Palindrome) hay không (không phân biệt chữ hoa, chữ thường và bỏ qua khoảng trắng).
"""

s = input("Nhập chuỗi: ")

dao_nguoc = s[::-1]
print(f"Chuoi dao nguoc: {dao_nguoc}")

# Chuẩn hóa để kiểm tra đối xứng
clean_s = s.replace(" ", "").lower()
if clean_s == clean_s[::-1]:
    print("Chuoi doi xung")
else:
    print("Khong doi xung")
