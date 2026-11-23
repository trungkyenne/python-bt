# Dem so ngay co doanh thu bang 0
n = int(input("Nhap so ngay can thong ke: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

so_ngay_0 = sum(1 for dt in doanh_thu if dt == 0)
print(f"So ngay co doanh thu bang 0 la: {so_ngay_0}")
