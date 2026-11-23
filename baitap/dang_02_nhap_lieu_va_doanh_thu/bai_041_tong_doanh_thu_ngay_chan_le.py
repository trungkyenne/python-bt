# Tinh tong doanh thu ngay chan va ngay le (theo chi so ngay 1, 2, 3...)
n = int(input("Nhap so ngay: "))
doanh_thu = []
for i in range(n):
    tien = float(input(f"Nhap doanh thu ngay {i + 1}: "))
    doanh_thu.append(tien)

tong_le = 0.0
tong_chan = 0.0

for i, dt in enumerate(doanh_thu):
    ngay = i + 1
    if ngay % 2 != 0:
        tong_le += dt
    else:
        tong_chan += dt

print(f"Tong doanh thu cac ngay le: {tong_le:.2f}")
print(f"Tong doanh thu cac ngay chan: {tong_chan:.2f}")
