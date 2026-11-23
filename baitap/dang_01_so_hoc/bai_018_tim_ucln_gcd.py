# Tim uoc chung lon nhat (GCD)
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

x, y = abs(a), abs(b)
while y != 0:
    x, y = y, x % y

print(f"Uoc chung lon nhat cua {a} va {b} la: {x}")
