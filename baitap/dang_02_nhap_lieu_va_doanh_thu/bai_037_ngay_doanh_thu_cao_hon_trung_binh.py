# Tim ngay co doanh thu cao hon doanh thu trung binh
n = int(input("Nhap so ngay can thong ke: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

dt_tb = sum(doanh_thu) / n
print(f"Doanh thu trung binh: {dt_tb:.2f}")
print("Cac ngay co doanh thu cao hon trung binh:")
for i, dt in enumerate(doanh_thu):
    if dt > dt_tb:
        print(f"Ngay thu {i + 1}: {dt:.2f}")
