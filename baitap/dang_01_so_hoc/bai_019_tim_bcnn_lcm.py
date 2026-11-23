# Tim boi chung nho nhat (LCM)
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y
gcd = x

if gcd != 0:
    lcm = (abs(a) * abs(b)) // gcd
    print(f"Boi chung nho nhat cua {a} va {b} la: {lcm}")
else:
    print("Khong co boi chung nho nhat")
