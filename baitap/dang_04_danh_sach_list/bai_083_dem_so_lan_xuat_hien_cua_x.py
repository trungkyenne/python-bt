# Dem so lan xuat hien cua X trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

x = int(input("Nhap gia tri X can dem: "))
so_lan = ds.count(x)
print(f"Phan tu {x} xuat hien {so_lan} lan trong danh sach")
