# Tim ngay co doanh thu cao nhat trong tuan
thu_trong_tuan = ["Thu Hai", "Thu Ba", "Thu Tu", "Thu Nam", "Thu Sau", "Thu Bay", "Chu Nhat"]
doanh_thu = []

for thu in thu_trong_tuan:
    tien = float(input(f"Nhap doanh thu ngay {thu}: "))
    doanh_thu.append(tien)

max_dt = max(doanh_thu)
idx_max = doanh_thu.index(max_dt)
print(f"Ngay co doanh thu cao nhat la: {thu_trong_tuan[idx_max]} voi {max_dt:.2f}")
