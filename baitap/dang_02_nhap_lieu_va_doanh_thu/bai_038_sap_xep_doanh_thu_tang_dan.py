# Sap xep doanh thu theo thu tu tang dan
n = int(input("Nhap so ngay can thong ke: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

dt_tang_dan = sorted(doanh_thu)
print("Danh sach doanh thu theo thu tu tang dan:")
for dt in dt_tang_dan:
    print(f"{dt:.2f}", end=" ")
print()
