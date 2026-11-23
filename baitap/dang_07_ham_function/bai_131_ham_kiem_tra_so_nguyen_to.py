# Viet ham kiem tra so nguyen to
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Chuong trinh chinh
so = int(input("Nhap so can kiem tra: "))
if la_so_nguyen_to(so):
    print(f"{so} la so nguyen to")
else:
    print(f"{so} khong phai la so nguyen to")
