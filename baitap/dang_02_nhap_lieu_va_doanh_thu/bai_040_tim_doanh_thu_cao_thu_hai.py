# Tim ngay co doanh thu cao thu hai
n = int(input("Nhap so ngay can thong ke (n >= 2): "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay thu {i + 1}: "))
    doanh_thu.append(tien)

tap_dt = list(set(doanh_thu))
tap_dt.sort(reverse=True)

if len(tap_dt) >= 2:
    dt_thu_hai = tap_dt[1]
    print(f"Muc doanh thu cao thu hai la: {dt_thu_hai:.2f}")
    for i, dt in enumerate(doanh_thu):
        if dt == dt_thu_hai:
            print(f"Thuoc ngay thu {i + 1}")
else:
    print("Khong ton tai doanh thu cao thu hai (tat ca cac ngay deu bang nhau)")
