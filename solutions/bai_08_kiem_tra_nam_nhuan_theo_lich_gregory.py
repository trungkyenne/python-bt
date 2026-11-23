# -*- coding: utf-8 -*-
r"""
Bài 08: Kiểm tra năm nhuận theo lịch Gregory
Mức độ: Trung bình
Mục tiêu: Theo dương lịch (lịch Gregory), một năm được coi là năm nhuận nếu nó chia hết cho 400, hoặc chia hết cho 4 nhưng không chia hết cho 100. Hãy viết chương trình nhập vào một năm dương lịch $Y$ (nguyên dương) và thông báo năm đó có phải năm nhuận hay không.
"""

nam = int(input("Nhập năm: "))

if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print("Nam nhuan")
else:
    print("Nam khong nhuan")
