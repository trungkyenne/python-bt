# Nhap N phan tu vao danh sach
n = int(input("Nhap so luong phan tu N: "))
ds = []
for i in range(n):
    x = int(input(f"Nhap phan tu thu {i + 1}: "))
    ds.append(x)

print("Danh sach cac phan tu vua nhap la:")
print(ds)
