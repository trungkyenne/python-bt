# Kiem tra so nguyen to
n = int(input("Nhap so nguyen n: "))
if n < 2:
    print(f"So {n} khong phai la so nguyen to")
else:
    la_snt = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_snt = False
            break
    if la_snt:
        print(f"So {n} la so nguyen to")
    else:
        print(f"So {n} khong phai la so nguyen to")
