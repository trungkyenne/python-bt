# Sap xep doanh thu theo thu tu giam dan
n = int(input("Nhap so ngay can thong ke: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

dt_giam_dan = sorted(doanh_thu, reverse=True)
print("Danh sach doanh thu theo thu tu giam dan:")
for dt in dt_giam_dan:
    print(f"{dt:.2f}", end=" ")
print()
