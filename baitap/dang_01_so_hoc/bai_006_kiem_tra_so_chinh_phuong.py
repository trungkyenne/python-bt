# Kiem tra so chinh phuong
n = int(input("Nhap so nguyen n: "))
if n >= 0:
    can = int(n**0.5)
    if can * can == n:
        print(f"So {n} la so chinh phuong")
    else:
        print(f"So {n} khong phai la so chinh phuong")
else:
    print(f"So {n} khong phai la so chinh phuong (so am)")
