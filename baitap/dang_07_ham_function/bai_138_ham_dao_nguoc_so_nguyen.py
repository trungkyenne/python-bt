# Viet ham dao nguoc so nguyen
def dao_nguoc_so(n):
    dau = -1 if n < 0 else 1
    temp = abs(n)
    dao = 0
    while temp > 0:
        dao = dao * 10 + temp % 10
        temp //= 10
    return dao * dau

# Chuong trinh chinh
so = int(input("Nhap so can dao nguoc: "))
print(f"So dao nguoc cua {so} la: {dao_nguoc_so(so)}")
