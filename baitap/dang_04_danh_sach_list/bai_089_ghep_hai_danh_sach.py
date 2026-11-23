# Ghep hai danh sach
n1 = int(input("Nhap so luong phan tu danh sach 1: "))
ds1 = []
for i in range(n1):
    ds1.append(input(f"Nhap phan tu thu {i + 1} cua danh sach 1: "))

n2 = int(input("Nhap so luong phan tu danh sach 2: "))
ds2 = []
for i in range(n2):
    ds2.append(input(f"Nhap phan tu thu {i + 1} cua danh sach 2: "))

ds_ghep = ds1 + ds2
print("Danh sach sau khi ghep:")
print(ds_ghep)
