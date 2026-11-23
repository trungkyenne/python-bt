# Tinh tien thanh toan theo muc giam gia hoa don
tien = float(input("Nhap tong gia tri hoa don: "))

if tien >= 1000000:
    giam = tien * 0.15 # Giam 15%
elif tien >= 500000:
    giam = tien * 0.10 # Giam 10%
elif tien >= 200000:
    giam = tien * 0.05 # Giam 5%
else:
    giam = 0

thanh_toan = tien - giam
print(f"Tien duoc giam: {giam:.2f}")
print(f"Tien phai thanh toan: {thanh_toan:.2f}")
