# Xoa phan tu tai vi tri K
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(input(f"Nhap phan tu thu {i + 1}: "))

k = int(input("Nhap vi tri K can xoa (bat dau tu 0): "))
if 0 <= k < len(ds):
    pt_xoa = ds.pop(k)
    print(f"Da xoa phan tu '{pt_xoa}' tai vi tri {k}")
    print(f"Danh sach sau khi xoa: {ds}")
else:
    print("Vi tri K khong hop le")
