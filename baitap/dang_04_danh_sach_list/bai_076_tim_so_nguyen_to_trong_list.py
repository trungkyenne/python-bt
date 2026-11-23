# Tim cac so nguyen to trong danh sach
def kiem_tra_snt(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

snt = [x for x in ds if kiem_tra_snt(x)]
print(f"Cac so nguyen to trong danh sach la: {snt}")
