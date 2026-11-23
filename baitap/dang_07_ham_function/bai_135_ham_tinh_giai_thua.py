# Viet ham tinh giai thua
def tinh_giai_thua(n):
    if n < 0:
        return None
    gt = 1
    for i in range(1, n + 1):
        gt *= i
    return gt

# Chuong trinh chinh
so = int(input("Nhap so nguyen n: "))
kq = tinh_giai_thua(so)
if kq is not None:
    print(f"{so}! = {kq}")
else:
    print("Khong the tinh giai thua cho so am")
