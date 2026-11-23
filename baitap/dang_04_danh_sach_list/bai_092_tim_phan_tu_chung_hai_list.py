# Tim cac phan tu chung cua hai danh sach
n1 = int(input("Nhap so luong phan tu danh sach 1: "))
ds1 = [input(f"DS1 - phan tu {i + 1}: ") for i in range(n1)]

n2 = int(input("Nhap so luong phan tu danh sach 2: "))
ds2 = [input(f"DS2 - phan tu {i + 1}: ") for i in range(n2)]

chung = list(set(ds1) & set(ds2))
print("Cac phan tu chung cua hai danh sach la:")
print(chung)
