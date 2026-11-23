# Dem so phan tu chan va le trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

so_chan = sum(1 for x in ds if x % 2 == 0)
so_le = len(ds) - so_chan

print(f"So luong phan tu chan: {so_chan}")
print(f"So luong phan tu le: {so_le}")
