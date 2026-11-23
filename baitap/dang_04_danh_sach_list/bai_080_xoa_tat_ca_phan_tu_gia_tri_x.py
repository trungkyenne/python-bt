# Xoa tat ca phan tu co gia tri X
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

x = int(input("Nhap gia tri X can xoa: "))
ds_moi = [item for item in ds if item != x]
print(f"Danh sach sau khi xoa tat ca phan tu co gia tri {x}: {ds_moi}")
