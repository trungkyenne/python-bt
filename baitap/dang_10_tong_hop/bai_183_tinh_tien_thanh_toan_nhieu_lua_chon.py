# Chuong trinh tinh tien thanh toan voi nhieu hinh thuc thanh toan
tong_tien = float(input("Nhap tong gia tri don hang: "))
print("Chon hinh thuc thanh toan:")
print("1. Tien mat (Khong giam gia)")
print("2. Chuyen khoan / Vi dien tu (Giam 2%)")
print("3. The tin dung VIP (Giam 5%)")

chon = input("Nhap lua chon cua ban (1-3): ")
if chon == "2":
    giam = tong_tien * 0.02
elif chon == "3":
    giam = tong_tien * 0.05
else:
    giam = 0.0

thuc_thu = tong_tien - giam
print(f"Tien duoc giam: {giam:.2f}")
print(f"So tien thuc te can thanh toan: {thuc_thu:.2f}")
