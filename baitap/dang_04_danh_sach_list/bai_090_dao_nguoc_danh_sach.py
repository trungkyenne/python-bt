# Dao nguoc danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(input(f"Nhap phan tu thu {i + 1}: "))

ds_dao = ds[::-1]
print("Danh sach sau khi dao nguoc:")
print(ds_dao)
