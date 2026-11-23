# Dem so lan xuat hien cua chu so D trong so N
n = int(input("Nhap so nguyen N: "))
d = int(input("Nhap chu so can dem (0-9): "))

temp = abs(n)
dem = 0
if temp == 0 and d == 0:
    dem = 1
else:
    while temp > 0:
        if temp % 10 == d:
            dem += 1
        temp //= 10

print(f"Chu so {d} xuat hien {dem} lan trong so {n}")
