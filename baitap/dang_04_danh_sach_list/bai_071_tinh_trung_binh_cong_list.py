# Tinh trung binh cong cac phan tu
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

if len(ds) > 0:
    tbc = sum(ds) / len(ds)
    print(f"Trung binh cong cac phan tu la: {tbc:.2f}")
else:
    print("Danh sach rong")
