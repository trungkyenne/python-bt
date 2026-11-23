# Dem so phan tu am, duong, bang 0
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(float(input(f"Nhap phan tu thu {i + 1}: ")))

am = sum(1 for x in ds if x < 0)
duong = sum(1 for x in ds if x > 0)
khong = sum(1 for x in ds if x == 0)

print(f"So luong phan tu duong: {duong}")
print(f"So luong phan tu am: {am}")
print(f"So luong phan tu bang 0: {khong}")
