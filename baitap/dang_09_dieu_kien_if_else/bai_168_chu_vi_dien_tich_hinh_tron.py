# Tinh chu vi va dien tich hinh tron
import math
r = float(input("Nhap ban kinh r: "))
if r > 0:
    cv = 2 * math.pi * r
    dt = math.pi * r**2
    print(f"Chu vi hinh tron: {cv:.2f}")
    print(f"Dien tich hinh tron: {dt:.2f}")
else:
    print("Ban kinh phai lon hon 0")
