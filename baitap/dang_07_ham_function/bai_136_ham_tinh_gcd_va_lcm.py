# Viet ham tinh GCD va LCM
def tim_gcd(a, b):
    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    return x

def tim_lcm(a, b):
    gcd = tim_gcd(a, b)
    if gcd == 0:
        return 0
    return (abs(a) * abs(b)) // gcd

# Chuong trinh chinh
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))
print(f"UCLN (GCD) cua {a} va {b} la: {tim_gcd(a, b)}")
print(f"BCNN (LCM) cua {a} va {b} la: {tim_lcm(a, b)}")
