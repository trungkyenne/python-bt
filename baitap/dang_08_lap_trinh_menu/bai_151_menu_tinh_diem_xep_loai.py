# Menu tinh diem va xep loai hoc luc
toan = float(input("Nhap diem Toan: "))
ly = float(input("Nhap diem Ly: "))
hoa = float(input("Nhap diem Hoa: "))

dtb = (toan + ly + hoa) / 3
print(f"Diem trung binh 3 mon: {dtb:.2f}")

if dtb >= 8.5:
    loai = "Gioi"
elif dtb >= 6.5:
    loai = "Kha"
elif dtb >= 5.0:
    loai = "Trung Binh"
else:
    loai = "Yeu"

print(f"Xep loai hoc luc: {loai}")
