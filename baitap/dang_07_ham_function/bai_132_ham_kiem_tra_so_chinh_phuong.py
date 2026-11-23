# Viet ham kiem tra so chinh phuong
def la_so_chinh_phuong(n):
    if n < 0:
        return False
    can = int(n**0.5)
    return can * can == n

# Chuong trinh chinh
so = int(input("Nhap so can kiem tra: "))
if la_so_chinh_phuong(so):
    print(f"{so} la so chinh phuong")
else:
    print(f"{so} khong phai la so chinh phuong")
