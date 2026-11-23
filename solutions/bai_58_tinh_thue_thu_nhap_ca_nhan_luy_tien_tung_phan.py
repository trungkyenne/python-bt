# -*- coding: utf-8 -*-
r"""
Bài 58: Tính thuế thu nhập cá nhân lũy tiến từng phần
Mức độ: Khó
Mục tiêu: Thuế thu nhập cá nhân (TNCN) đối với thu nhập từ tiền lương được tính theo biểu thuế lũy tiến từng phần sau khi đã trừ đi các khoản giảm trừ:\n- Giảm trừ bản thân: 11 triệu đồng/tháng.\n- Giảm trừ người phụ thuộc: 4.4 triệu đồng/người/tháng.\nThu nhập tính thuế (TNTT) = Tổng thu nhập - Các khoản giảm trừ (nếu $\le 0$ thì thuế = 0).\nBiểu thuế lũy tiến:\n+ Bậc 1: Đến 5 triệu: thuế suất 5%\n+ Bậc 2: Trên 5 đến 10 triệu: thuế suất 10%\n+ Bậc 3: Trên 10 đến 18 triệu: thuế suất 15%\n+ Bậc 4: Trên 18 đến 32 triệu: thuế suất 20%\n+ Bậc 5: Trên 32 đến 52 triệu: thuế suất 25%\n+ Bậc 6: Trên 52 đến 80 triệu: thuế suất 30%\n+ Bậc 7: Trên 80 triệu: thuế suất 35%\nViết chương trình nhập Tổng thu nhập hàng tháng và Số người phụ thuộc, tính và in ra Thu nhập tính thuế và Số tiền thuế phải nộp.
"""

tong_tn = float(input("Nhập tổng thu nhập: "))
so_pt = int(input("Nhập số người phụ thuộc: "))

giam_tru = 11000000 + so_pt * 4400000
tntt = max(0.0, tong_tn - giam_tru)

thue = 0.0
# Các ngưỡng bậc tính thuế (triệu đồng)
if tntt <= 0:
    thue = 0.0
elif tntt <= 5000000:
    thue = tntt * 0.05
elif tntt <= 10000000:
    thue = 5000000 * 0.05 + (tntt - 5000000) * 0.10
elif tntt <= 18000000:
    thue = 5000000 * 0.05 + 5000000 * 0.10 + (tntt - 10000000) * 0.15
elif tntt <= 32000000:
    thue = 5000000 * 0.05 + 5000000 * 0.10 + 8000000 * 0.15 + (tntt - 18000000) * 0.20
elif tntt <= 52000000:
    thue = (5000000*0.05 + 5000000*0.10 + 8000000*0.15 + 14000000*0.20 + 
            (tntt - 32000000) * 0.25)
elif tntt <= 80000000:
    thue = (5000000*0.05 + 5000000*0.10 + 8000000*0.15 + 14000000*0.20 + 
            20000000*0.25 + (tntt - 52000000) * 0.30)
else:
    thue = (5000000*0.05 + 5000000*0.10 + 8000000*0.15 + 14000000*0.20 + 
            20000000*0.25 + 28000000*0.30 + (tntt - 80000000) * 0.35)

print(f"Thu nhap tinh thue: {round(tntt)} VND")
print(f"Thue TNCN phai nop: {round(thue)} VND")
