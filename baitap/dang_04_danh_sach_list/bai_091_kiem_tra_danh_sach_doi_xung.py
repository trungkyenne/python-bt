# Kiem tra danh sach doi xung
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(input(f"Nhap phan tu thu {i + 1}: "))

if ds == ds[::-1]:
    print("Danh sach la doi xung (Palindrome)")
else:
    print("Danh sach khong doi xung")
