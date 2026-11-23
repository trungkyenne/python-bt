# Viet ham tinh tong cac chu so
def tong_chu_so(n):
    temp = abs(n)
    tong = 0
    while temp > 0:
        tong += temp % 10
        temp //= 10
    return tong

# Chuong trinh chinh
so = int(input("Nhap so can tinh tong chu so: "))
print(f"Tong cac chu so cua {so} la: {tong_chu_so(so)}")
