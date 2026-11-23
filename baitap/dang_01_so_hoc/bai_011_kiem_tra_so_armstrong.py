# Kiem tra so Armstrong
n = int(input("Nhap so nguyen duong n: "))
chu_so = str(n)
k = len(chu_so)
tong_luy_thua = sum(int(c)**k for c in chu_so)

if tong_luy_thua == n:
    print(f"So {n} la so Armstrong")
else:
    print(f"So {n} khong phai la so Armstrong")
