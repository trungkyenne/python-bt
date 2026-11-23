# Tinh thue thu nhap ca nhan theo muc thu nhap
thu_nhap = float(input("Nhap tong thu nhap tinh thue (VND): "))

if thu_nhap <= 5000000:
    thue = thu_nhap * 0.05
elif thu_nhap <= 10000000:
    thue = 5000000 * 0.05 + (thu_nhap - 5000000) * 0.10
else:
    thue = 5000000 * 0.05 + 5000000 * 0.10 + (thu_nhap - 10000000) * 0.15

print(f"Tien thue phai nop: {thue:.2f} VND")
