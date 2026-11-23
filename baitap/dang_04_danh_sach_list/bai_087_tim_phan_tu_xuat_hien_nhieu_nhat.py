# Tim cac phan tu xuat hien nhieu nhat trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

dem = {}
for x in ds:
    dem[x] = dem.get(x, 0) + 1

max_dem = max(dem.values())
pho_bien = [k for k, v in dem.items() if v == max_dem]

print(f"So lan xuat hien nhieu nhat la: {max_dem} lan")
print(f"Cac phan tu xuat hien nhieu nhat la: {pho_bien}")
