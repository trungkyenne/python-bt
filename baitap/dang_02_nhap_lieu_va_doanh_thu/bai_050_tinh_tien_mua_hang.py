# Tinh tien mua hang theo so luong va don gia
ten_hang = input("Nhap ten mat hang: ")
so_luong = int(input("Nhap so luong can mua: "))
don_gia = float(input("Nhap don gia: "))

tong_tien = so_luong * don_gia
# Uu dai neu mua tu 10 san pham tro len duoc giam 5%
if so_luong >= 10:
    giam_gia = tong_tien * 0.05
    thanh_toan = tong_tien - giam_gia
    print(f"Duoc giam gia 5% ({giam_gia:.2f} VND)")
else:
    thanh_toan = tong_tien

print(f"Tong tien thanh toan cho {so_luong} {ten_hang} la: {thanh_toan:.2f} VND")
