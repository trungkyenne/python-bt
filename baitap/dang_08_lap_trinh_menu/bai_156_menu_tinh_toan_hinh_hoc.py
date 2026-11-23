# Menu tinh toan hinh hoc
print("=== MENU HINH HOC ===")
print("1. Hinh chu nhat")
print("2. Hinh tron")
print("3. Hinh vuong")
chon = input("Nhap lua chon: ")

if chon == "1":
    d = float(input("Nhap chieu dai: "))
    r = float(input("Nhap chieu rong: "))
    print(f"Chu vi: {2 * (d + r):.2f}, Dien tich: {d * r:.2f}")
elif chon == "2":
    import math
    bk = float(input("Nhap ban kinh: "))
    print(f"Chu vi: {2 * math.pi * bk:.2f}, Dien tich: {math.pi * bk**2:.2f}")
elif chon == "3":
    c = float(input("Nhap canh hinh vuong: "))
    print(f"Chu vi: {4 * c:.2f}, Dien tich: {c**2:.2f}")
else:
    print("Lua chon khong hop le")
