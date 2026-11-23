# Tim ngay co doanh thu thap nhat trong tuan
thu_trong_tuan = ["Thu Hai", "Thu Ba", "Thu Tu", "Thu Nam", "Thu Sau", "Thu Bay", "Chu Nhat"]
doanh_thu = []

for thu in thu_trong_tuan:
    tien = float(input(f"Nhap doanh thu ngay {thu}: "))
    doanh_thu.append(tien)

min_dt = min(doanh_thu)
idx_min = doanh_thu.index(min_dt)
print(f"Ngay co doanh thu thap nhat la: {thu_trong_tuan[idx_min]} voi {min_dt:.2f}")
