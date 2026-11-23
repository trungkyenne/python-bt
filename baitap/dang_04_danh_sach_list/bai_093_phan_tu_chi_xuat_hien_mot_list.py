# Tim cac phan tu chi xuat hien trong mot trong hai danh sach (hieu doi xung)
n1 = int(input("Nhap so luong phan tu danh sach 1: "))
ds1 = [input(f"DS1 - phan tu {i + 1}: ") for i in range(n1)]

n2 = int(input("Nhap so luong phan tu danh sach 2: "))
ds2 = [input(f"DS2 - phan tu {i + 1}: ") for i in range(n2)]

chi_mot_ds = list(set(ds1) ^ set(ds2))
print("Cac phan tu chi xuat hien trong mot danh sach duy nhat la:")
print(chi_mot_ds)
