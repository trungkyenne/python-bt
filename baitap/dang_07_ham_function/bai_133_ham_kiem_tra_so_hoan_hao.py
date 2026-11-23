# Viet ham kiem tra so hoan hao
def la_so_hoan_hao(n):
    if n <= 1:
        return False
    tong = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong == n

# Chuong trinh chinh
so = int(input("Nhap so can kiem tra: "))
if la_so_hoan_hao(so):
    print(f"{so} la so hoan hao")
else:
    print(f"{so} khong phai la so hoan hao")
