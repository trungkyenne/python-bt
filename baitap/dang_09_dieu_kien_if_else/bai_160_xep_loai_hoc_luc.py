# Xep loai hoc luc theo diem trung binh
diem = float(input("Nhap diem trung binh: "))
if diem >= 9.0:
    loai = "Xuat sac"
elif diem >= 8.0:
    loai = "Gioi"
elif diem >= 6.5:
    loai = "Kha"
elif diem >= 5.0:
    loai = "Trung binh"
else:
    loai = "Yeu"
print(f"Xep loai: {loai}")
