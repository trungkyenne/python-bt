# -*- coding: utf-8 -*-
r"""
Bài 09: Xác định loại tam giác và tính diện tích theo công thức Heron
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào độ dài 3 cạnh $a, b, c$ của một hình học. Hãy kiểm tra xem 3 cạnh đó có tạo thành một tam giác hợp lệ hay không. Nếu hợp lệ, hãy cho biết đó là tam giác đều, tam giác cân, tam giác vuông hay tam giác thường, và tính diện tích tam giác theo công thức Heron. Nếu không hợp lệ, in ra thông báo 'Khong phai tam giac'.
"""

a, b, c = map(float, input("Nhập độ dài 3 cạnh: ").split())

# Kiểm tra điều kiện tồn tại tam giác
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    # Xác định loại tam giác
    eps = 1e-6
    is_vuong = (abs(a**2 + b**2 - c**2) < eps or 
                abs(a**2 + c**2 - b**2) < eps or 
                abs(b**2 + c**2 - a**2) < eps)
    
    if a == b == c:
        loai = "Tam giac deu"
    elif is_vuong:
        loai = "Tam giac vuong"
    elif a == b or b == c or c == a:
        loai = "Tam giac can"
    else:
        loai = "Tam giac thuong"
        
    p = (a + b + c) / 2
    dien_tich = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    
    print(loai)
    print(f"Dien tich: {dien_tich:.2f}")
else:
    print("Khong phai tam giac")
