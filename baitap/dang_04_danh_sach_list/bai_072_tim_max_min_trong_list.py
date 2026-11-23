# Tim phan tu lon nhat va nho nhat trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

if len(ds) > 0:
    print(f"Phan tu lon nhat la: {max(ds):.2f}")
    print(f"Phan tu nho nhat la: {min(ds):.2f}")
else:
    print("Danh sach rong")
