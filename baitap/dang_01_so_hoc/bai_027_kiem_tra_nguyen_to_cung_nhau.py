# Tim so nguyen to cung nhau (GCD = 1)
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y

if x == 1:
    print(f"{a} va {b} la hai so nguyen to cung nhau")
else:
    print(f"{a} va {b} khong phai la hai so nguyen to cung nhau (UCLN = {x})")
