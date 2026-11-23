# Quan ly diem va xep loai sinh vien
n = int(input("Nhap so luong sinh vien: "))
danh_sach = []

for i in range(n):
    ten = input(f"Nhap ho ten sinh vien {i + 1}: ")
    diem = float(input(f"Nhap diem cua {ten}: "))
    if diem >= 8.5:
        loai = "Gioi"
    elif diem >= 6.5:
        loai = "Kha"
    elif diem >= 5.0:
        loai = "Trung Binh"
    else:
        loai = "Yeu"
    danh_sach.append({"ten": ten, "diem": diem, "loai": loai})

print("\n--- BANG XEP LOAI SINH VIEN ---")
for sv in danh_sach:
    print(f"{sv['ten']} - Diem: {sv['diem']:.2f} - Xep loai: {sv['loai']}")
