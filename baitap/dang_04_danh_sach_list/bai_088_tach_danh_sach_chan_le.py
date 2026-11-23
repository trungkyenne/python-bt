# Tach danh sach thanh danh sach chan va le
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

ds_chan = [x for x in ds if x % 2 == 0]
ds_le = [x for x in ds if x % 2 != 0]

print(f"Danh sach so chan ({len(ds_chan)} phan tu): {ds_chan}")
print(f"Danh sach so le ({len(ds_le)} phan tu): {ds_le}")
