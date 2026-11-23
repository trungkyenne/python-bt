# Nhap doanh thu tung ngay trong tuan, tinh tong doanh thu
thu_trong_tuan = ["Thu Hai", "Thu Ba", "Thu Tu", "Thu Nam", "Thu Sau", "Thu Bay", "Chu Nhat"]
doanh_thu = []

for thu in thu_trong_tuan:
    tien = float(input(f"Nhap doanh thu ngay {thu}: "))
    doanh_thu.append(tien)

tong_dt = sum(doanh_thu)
print(f"Tong doanh thu trong tuan la: {tong_dt:.2f}")
