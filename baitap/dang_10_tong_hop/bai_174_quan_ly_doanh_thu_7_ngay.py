# Quan ly doanh thu ban hang trong 7 ngay
cac_ngay = ["Thu 2", "Thu 3", "Thu 4", "Thu 5", "Thu 6", "Thu 7", "Chu Nhat"]
doanh_thu = []

for ngay in cac_ngay:
    dt = float(input(f"Nhap doanh thu ngay {ngay}: "))
    doanh_thu.append(dt)

tong = sum(doanh_thu)
tb = tong / 7
max_dt = max(doanh_thu)
ngay_max = cac_ngay[doanh_thu.index(max_dt)]

print("\n--- KET QUA THONG KE ---")
print(f"Tong doanh thu trong 7 ngay: {tong:.2f}")
print(f"Doanh thu trung binh moi ngay: {tb:.2f}")
print(f"Ngay dat doanh thu cao nhat: {ngay_max} ({max_dt:.2f})")
