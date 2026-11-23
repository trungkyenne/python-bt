# Tinh chu vi va dien tich tam giac theo cong thuc Heron
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c) / 2
    cv = a + b + c
    dt = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f"Chu vi tam giac: {cv:.2f}")
    print(f"Dien tich tam giac: {dt:.2f}")
else:
    print("Ba canh khong tao thanh tam giac")
