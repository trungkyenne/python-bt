# Tinh tien nuoc theo muc tieu thu (m3)
m3 = float(input("Nhap so m3 nuoc tieu thu: "))

# Den 10m3 dau: 6000 VND/m3
# Tu 10m3 den 20m3: 7500 VND/m3
# Tren 20m3: 9000 VND/m3
if m3 <= 10:
    tien = m3 * 6000
elif m3 <= 20:
    tien = 10 * 6000 + (m3 - 10) * 7500
else:
    tien = 10 * 6000 + 10 * 7500 + (m3 - 20) * 9000

print(f"Tien nuoc tieu thu ({m3} m3) la: {tien:.2f} VND")
