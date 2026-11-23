# -*- coding: utf-8 -*-
r"""
Bài 24: Mô phỏng trò chơi đoán số ngẫu nhiên
Mức độ: Khó
Mục tiêu: Viết chương trình mô phỏng trò chơi đoán số: Máy tính có một số bí mật $K$ được nhập vào trước (hoặc giả lập số bí mật từ 1 đến 100). Sau đó, người chơi sẽ lần lượt nhập các số dự đoán. Nếu số nhập vào nhỏ hơn số bí mật, in 'Lon hon'. Nếu lớn hơn số bí mật, in 'Nho hon'. Nếu đoán trúng, in 'Chinh xac!' cùng số lần dự đoán và kết thúc chương trình.
"""

k = int(input("Nhập số bí mật K: "))
so_lan = 0

while True:
    doan = int(input("Nhập số dự đoán: "))
    so_lan += 1
    if doan < k:
        print("Lon hon")
    elif doan > k:
        print("Nho hon")
    else:
        print(f"Chinh xac! So lan doan: {so_lan}")
        break
