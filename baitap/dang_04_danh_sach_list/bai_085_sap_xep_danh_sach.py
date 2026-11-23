# Sap xep danh sach tang dan, giam dan
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

ds_tang = sorted(ds)
ds_giam = sorted(ds, reverse=True)

print("Danh sach tang dan:", ds_tang)
print("Danh sach giam dan:", ds_giam)
