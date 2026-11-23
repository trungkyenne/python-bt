# -*- coding: utf-8 -*-
r"""
Bài 60: Chương trình mô phỏng máy rút tiền tự động ATM
Mức độ: Khó
Mục tiêu: Một cây ATM hiện có các loại tiền mệnh giá: 500.000đ, 200.000đ, 100.000đ và 50.000đ với số lượng không hạn chế. Khách hàng nhập vào số tiền cần rút $S$ (nguyên dương, là bội số của 50.000đ). Hãy viết chương trình:\n1. Kiểm tra tính hợp lệ của số tiền rút (nếu $S \le 0$ hoặc không chia hết cho 50.000đ, in thông báo lỗi 'So tien khong hop le').\n2. Nếu hợp lệ, hãy áp dụng giải thuật tham lam (Greedy Algorithm) để chi trả số tiền trên sao cho tổng số tờ tiền đưa ra là ít nhất.\n3. In chi tiết số lượng tờ tiền của từng mệnh giá và tổng số tờ tiền đã phát.
"""

s = int(input("Nhập số tiền cần rút: "))

if s <= 0 or s % 50000 != 0:
    print("So tien khong hop le")
else:
    menh_gia = [500000, 200000, 100000, 50000]
    chi_tiet = {}
    tong_so_to = 0
    con_lai = s
    
    for d in menh_gia:
        so_to = con_lai // d
        if so_to > 0:
            chi_tiet[d] = so_to
            tong_so_to += so_to
            con_lai %= d
            
    for d, to in chi_tiet.items():
        print(f"{d} VND: {to} to")
    print(f"Tong so to: {tong_so_to}")
