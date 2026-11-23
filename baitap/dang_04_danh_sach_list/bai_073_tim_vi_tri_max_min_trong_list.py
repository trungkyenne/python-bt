# Tim vi tri (chi so bat dau tu 0) cua phan tu lon nhat va nho nhat
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

if len(ds) > 0:
    max_val = max(ds)
    min_val = min(ds)
    idx_max = ds.index(max_val)
    idx_min = ds.index(min_val)
    print(f"Phan tu lon nhat {max_val:.2f} tai vi tri index: {idx_max}")
    print(f"Phan tu nho nhat {min_val:.2f} tai vi tri index: {idx_min}")
else:
    print("Danh sach rong")
