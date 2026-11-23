# Quan ly hoa don ban hang (in hoa don chi tiet)
khach = input("Nhap ten khach hang: ")
so_mon = int(input("Nhap so luong mat hang khach mua: "))
chi_tiet = []
tong_tien = 0.0

for i in range(so_mon):
    ten_mon = input(f"Nhap ten mon hang {i + 1}: ")
    sl = int(input(f"Nhap so luong {ten_mon}: "))
    gia = float(input(f"Nhap don gia: "))
    tien = sl * gia
    tong_tien += tien
    chi_tiet.append((ten_mon, sl, gia, tien))

print(f"\n========= HOA DON BAN HANG =========")
print(f"Khach hang: {khach}")
for mon, sl, gia, tien in chi_tiet:
    print(f"- {mon}: {sl} x {gia:.2f} = {tien:.2f}")
print(f"Tong cong: {tong_tien:.2f} VND")
print("====================================")
