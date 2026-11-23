# Tim kiem phan tu trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

x = int(input("Nhap phan tu can tim: "))
if x in ds:
    print(f"Phan tu {x} co trong danh sach tai vi tri dau tien la {ds.index(x)}")
else:
    print(f"Phan tu {x} khong co trong danh sach")
