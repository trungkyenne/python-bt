# -*- coding: utf-8 -*-
r"""
Bài 19: Nhập dữ liệu với vòng lặp while kèm điều kiện dừng
Mức độ: Trung bình
Mục tiêu: Viết chương trình liên tục nhận các số nguyên từ bàn phím cho đến khi người dùng nhập vào số 0 thì dừng lại. Sau khi dừng, in ra: Số lượng số đã nhập (không tính số 0), Tổng các số đã nhập và Giá trị trung bình cộng của các số đã nhập (lấy 2 chữ số thập phân). Nếu không nhập số nào ngoài số 0, thông báo 'Khong co du lieu'.
"""

count = 0
tong = 0

while True:
    x = int(input("Nhập số nguyên (0 để dừng): "))
    if x == 0:
        break
    count += 1
    tong += x

if count == 0:
    print("Khong co du lieu")
else:
    tb = tong / count
    print(f"So luong: {count}")
    print(f"Tong: {tong}")
    print(f"Trung binh: {tb:.2f}")
