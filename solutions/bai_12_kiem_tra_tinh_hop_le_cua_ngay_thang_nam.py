# -*- coding: utf-8 -*-
r"""
Bài 12: Kiểm tra tính hợp lệ của ngày, tháng, năm
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào 3 số nguyên $d, m, y$ đại diện cho ngày, tháng, năm. Hãy kiểm tra xem bộ ngày tháng năm đó có hợp lệ hay không. Chú ý xét năm nhuận đối với tháng 2 (tháng 2 năm nhuận có 29 ngày, năm thường có 28 ngày; các tháng 1, 3, 5, 7, 8, 10, 12 có 31 ngày; các tháng 4, 6, 9, 11 có 30 ngày).
"""

d, m, y = map(int, input("Nhập ngày tháng năm: ").split())

if y < 1 or m < 1 or m > 12:
    print("Khong hop le")
else:
    # Xác định năm nhuận
    is_nhuan = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31
    elif m in [4, 6, 9, 11]:
        max_d = 30
    else: # Tháng 2
        max_d = 29 if is_nhuan else 28
        
    if 1 <= d <= max_d:
        print("Hop le")
    else:
        print("Khong hop le")
