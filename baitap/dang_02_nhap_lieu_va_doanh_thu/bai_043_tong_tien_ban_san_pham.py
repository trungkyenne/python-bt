# Nhap doanh thu nhieu san pham va tinh tong tien ban duoc
m = int(input("Nhap so luong loai san pham: "))
tong_tien = 0.0

for i in range(m):
    ten_sp = input(f"Nhap ten san pham thu {i + 1}: ")
    so_luong = int(input(f"Nhap so luong da ban cua {ten_sp}: "))
    don_gia = float(input(f"Nhap don gia cua {ten_sp}: "))
    thanh_tien = so_luong * don_gia
    tong_tien += thanh_tien
    print(f"Thanh tien {ten_sp}: {thanh_tien:.2f}")

print(f"Tong tien ban duoc cua tat ca san pham: {tong_tien:.2f}")
