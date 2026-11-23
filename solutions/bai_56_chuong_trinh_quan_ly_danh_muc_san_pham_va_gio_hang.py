# -*- coding: utf-8 -*-
r"""
Bài 56: Chương trình quản lý danh mục sản phẩm và giỏ hàng
Mức độ: Trung bình
Mục tiêu: Một cửa hàng quản lý danh mục sản phẩm gồm Tên sản phẩm, Đơn giá và Số lượng tồn kho. Hãy viết chương trình cho phép:\n1. Nhập danh mục $M$ mặt hàng.\n2. Nhập danh sách mua hàng gồm Tên sản phẩm và Số lượng mua.\n3. Kiểm tra nếu mặt hàng không có trong kho thì in thông báo lỗi, nếu số lượng mua vượt quá tồn kho thì in thông báo không đủ hàng. Nếu hợp lệ, trừ tồn kho và tính tổng tiền hóa đơn.
"""

m = int(input("Nhập số mặt hàng trong kho: "))
kho = {}

for _ in range(m):
    ten, gia, ton = input().split()
    kho[ten] = {"gia": int(gia), "ton": int(ton)}

k = int(input("Nhập số mặt hàng muốn mua: "))
tong_tien = 0

for _ in range(k):
    ten_mua, sl_mua_str = input().split()
    sl_mua = int(sl_mua_str)
    
    if ten_mua not in kho:
        print(f"San pham {ten_mua} khong ton tai")
    elif kho[ten_mua]["ton"] < sl_mua:
        print(f"Kho khong du so luong cho {ten_mua}")
    else:
        kho[ten_mua]["ton"] -= sl_mua
        thanh_tien = sl_mua * kho[ten_mua]["gia"]
        tong_tien += thanh_tien
        print(f"Mua thanh cong {sl_mua} {ten_mua}")

print(f"Tong tien thanh toan: {tong_tien} VND")
