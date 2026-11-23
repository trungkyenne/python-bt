# Menu chuyen doi don vi do
print("=== MENU CHUYEN DOI DON VI ===")
print("1. Celsius sang Fahrenheit")
print("2. Met sang Centimet")
print("3. Kilogram sang Gram")
chon = input("Nhap lua chon: ")

if chon == "1":
    c = float(input("Nhap do C: "))
    print(f"Nhiet do F: {c * 1.8 + 32:.2f}")
elif chon == "2":
    m = float(input("Nhap so met: "))
    print(f"Centimet: {m * 100:.2f} cm")
elif chon == "3":
    kg = float(input("Nhap so kg: "))
    print(f"Gram: {kg * 1000:.2f} g")
else:
    print("Lua chon khong hop le")
