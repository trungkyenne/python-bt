# Menu kiem tra tinh chat so nguyen
def la_snt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

print("=== MENU KIEM TRA SO NGUYEN ===")
print("1. Kiem tra so chan / le")
print("2. Kiem tra so nguyen to")
print("3. Kiem tra so chinh phuong")
print("4. Kiem tra so hoan hao")

chon = input("Nhap lua chon (1-4): ")
n = int(input("Nhap so nguyen n can kiem tra: "))

if chon == "1":
    print(f"{n} la so chan" if n % 2 == 0 else f"{n} la so le")
elif chon == "2":
    print(f"{n} la so nguyen to" if la_snt(n) else f"{n} khong phai so nguyen to")
elif chon == "3":
    can = int(n**0.5) if n >= 0 else -1
    print(f"{n} la so chinh phuong" if can * can == n else f"{n} khong phai so chinh phuong")
elif chon == "4":
    tong = sum(i for i in range(1, n) if n % i == 0) if n > 1 else 0
    print(f"{n} la so hoan hao" if tong == n else f"{n} khong phai so hoan hao")
else:
    print("Lua chon khong hop le")
