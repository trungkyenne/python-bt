# Dem so ngay co doanh thu vuot muc X
n = int(input("Nhap so ngay can thong ke: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

muc_x = float(input("Nhap muc doanh thu X: "))
so_ngay_vuot = sum(1 for dt in doanh_thu if dt > muc_x)
print(f"So ngay co doanh thu vuot muc {muc_x:.2f} la: {so_ngay_vuot}")
