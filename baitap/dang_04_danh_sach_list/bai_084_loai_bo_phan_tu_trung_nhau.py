# Loai bo cac phan tu trung nhau (giu nguyen thu tu xuat hien dau tien)
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

ds_duy_nhat = []
seen = set()
for x in ds:
    if x not in seen:
        ds_duy_nhat.append(x)
        seen.add(x)

print(f"Danh sach sau khi loai bo cac phan tu trung nhau: {ds_duy_nhat}")
