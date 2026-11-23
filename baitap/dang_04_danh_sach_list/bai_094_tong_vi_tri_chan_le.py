# Tinh tong cac phan tu o vi tri (index) chan va le
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

tong_idx_chan = sum(ds[i] for i in range(0, len(ds), 2))
tong_idx_le = sum(ds[i] for i in range(1, len(ds), 2))

print(f"Tong cac phan tu tai vi tri index chan: {tong_idx_chan:.2f}")
print(f"Tong cac phan tu tai vi tri index le: {tong_idx_le:.2f}")
