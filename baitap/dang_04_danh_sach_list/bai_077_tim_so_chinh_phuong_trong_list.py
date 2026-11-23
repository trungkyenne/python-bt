# Tim cac so chinh phuong trong danh sach
def kiem_tra_cp(num):
    if num < 0:
        return False
    can = int(num**0.5)
    return can * can == num

n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

cp = [x for x in ds if kiem_tra_cp(x)]
print(f"Cac so chinh phuong trong danh sach la: {cp}")
