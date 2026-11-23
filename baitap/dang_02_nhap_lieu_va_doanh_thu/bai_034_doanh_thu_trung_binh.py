# Tinh doanh thu trung binh moi ngay trong tuan
thu_trong_tuan = ["Thu Hai", "Thu Ba", "Thu Tu", "Thu Nam", "Thu Sau", "Thu Bay", "Chu Nhat"]
doanh_thu = []

for thu in thu_trong_tuan:
    tien = float(input(f"Nhap doanh thu ngay {thu}: "))
    doanh_thu.append(tien)

dt_tb = sum(doanh_thu) / len(doanh_thu)
print(f"Doanh thu trung binh moi ngay la: {dt_tb:.2f}")
