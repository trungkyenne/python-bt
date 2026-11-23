# Tinh tong cac phan tu trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

tong = sum(ds)
print(f"Tong cac phan tu trong danh sach la: {tong:.2f}")
