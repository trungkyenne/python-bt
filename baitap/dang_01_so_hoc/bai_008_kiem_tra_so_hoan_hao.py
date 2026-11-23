# Kiem tra so hoan hao (tong uoc thuc su bang chinh no)
n = int(input("Nhap so nguyen n: "))
if n <= 1:
    print(f"So {n} khong phai la so hoan hao")
else:
    tong_uoc = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            tong_uoc += i
            if i != n // i:
                tong_uoc += n // i
    if tong_uoc == n:
        print(f"So {n} la so hoan hao")
    else:
        print(f"So {n} khong phai la so hoan hao")
