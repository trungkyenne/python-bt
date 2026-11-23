# -*- coding: utf-8 -*-
r"""
Bài 11: Tính tiền điện sinh hoạt theo bậc thang lũy tiến
Mức độ: Khó
Mục tiêu: Biểu giá bán lẻ điện sinh hoạt được tính theo các bậc lũy tiến như sau:\n- Bậc 1: Cho kWh từ 0 - 50: giá 1.678 đ/kWh\n- Bậc 2: Cho kWh từ 51 - 100: giá 1.734 đ/kWh\n- Bậc 3: Cho kWh từ 101 - 200: giá 2.014 đ/kWh\n- Bậc 4: Cho kWh từ 201 trở lên: giá 2.536 đ/kWh\nSau khi tính tiền điện theo bậc thang, khách hàng phải đóng thêm 8% thuế GTGT (VAT).\nViết chương trình nhập số kWh tiêu thụ (số nguyên không âm), tính và in ra: Tiền điện chưa thuế, Tiền thuế VAT và Tổng tiền phải thanh toán (làm tròn số nguyên).
"""

kwh = int(input("Nhập số kWh tiêu thụ: "))

if kwh <= 50:
    tien_dien = kwh * 1678
elif kwh <= 100:
    tien_dien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien_dien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
else:
    tien_dien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536

thue_vat = round(tien_dien * 0.08)
tong_cong = round(tien_dien + thue_vat)

print(f"Tien dien: {round(tien_dien)} VND")
print(f"Thue VAT: {thue_vat} VND")
print(f"Tong thanh toan: {tong_cong} VND")
