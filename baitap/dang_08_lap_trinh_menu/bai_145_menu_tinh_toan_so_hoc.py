# Menu tinh toan so hoc
print("=== MENU TINH TOAN SO HOC ===")
print("1. Tinh tong cac chu so")
print("2. Tinh giai thua N!")
print("3. Tim uoc chung lon nhat (GCD)")
print("4. Tim boi chung nho nhat (LCM)")

chon = input("Nhap lua chon (1-4): ")
if chon == "1":
    n = abs(int(input("Nhap so nguyen n: ")))
    tong = sum(int(c) for c in str(n))
    print(f"Tong cac chu so: {tong}")
elif chon == "2":
    n = int(input("Nhap so nguyen khong am n: "))
    gt = 1
    for i in range(1, n + 1): gt *= i
    print(f"{n}! = {gt}")
elif chon in ["3", "4"]:
    import math
    a = int(input("Nhap so a: "))
    b = int(input("Nhap so b: "))
    gcd = math.gcd(a, b)
    if chon == "3":
        print(f"UCLN cua {a} va {b} la: {gcd}")
    else:
        lcm = (abs(a) * abs(b)) // gcd if gcd != 0 else 0
        print(f"BCNN cua {a} va {b} la: {lcm}")
else:
    print("Lua chon khong hop le")
