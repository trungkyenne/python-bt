# Giai phuong trinh bac hai ax^2 + bx + c = 0
a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b == 0:
        print("Vo so nghiem" if c == 0 else "Vo nghiem")
    else:
        print(f"Nghiem x = {-c / b:.2f}")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phuong trinh vo nghiem")
    elif delta == 0:
        print(f"Phuong trinh co nghiem kep x = {-b / (2*a):.2f}")
    else:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
        print(f"Hai nghiem phan biet: x1 = {x1:.2f}, x2 = {x2:.2f}")
