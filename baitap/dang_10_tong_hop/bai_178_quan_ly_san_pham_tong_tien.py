# Quan ly danh sach san pham va tinh tong tien
m = int(input("Nhap so loai san pham: "))
san_pham = []
tong_tien = 0.0

for i in range(m):
    ten = input(f"Nhap ten san pham {i + 1}: ")
    sl = int(input(f"Nhap so luong ton kho cua {ten}: "))
    gia = float(input(f"Nhap don gia cua {ten}: "))
    thanh_tien = sl * gia
    tong_tien += thanh_tien
    san_pham.append({"ten": ten, "sl": sl, "gia": gia, "thanh_tien": thanh_tien})

print("\n--- DANH SACH KHO HANG ---")
for sp in san_pham:
    print(f"{sp['ten']}: So luong {sp['sl']} x {sp['gia']:.2f} = {sp['thanh_tien']:.2f}")
print(f"Tong gia tri kho hang: {tong_tien:.2f}")
