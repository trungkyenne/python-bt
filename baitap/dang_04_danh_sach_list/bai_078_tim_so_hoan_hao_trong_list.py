# Tim cac so hoan hao trong danh sach
def kiem_tra_hh(num):
    if num <= 1:
        return False
    tong = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tong += i
            if i != num // i:
                tong += num // i
    return tong == num

n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

hh = [x for x in ds if kiem_tra_hh(x)]
print(f"Cac so hoan hao trong danh sach la: {hh}")
