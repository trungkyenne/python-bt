# Menu tinh tien dien va nuoc sinh hoat
print("=== MENU TIEN DIEN NUOC ===")
print("1. Tinh tien dien")
print("2. Tinh tien nuoc")
chon = input("Nhap lua chon: ")

if chon == "1":
    kwh = float(input("Nhap so kWh dien: "))
    tien = kwh * 2000
    print(f"Tien dien: {tien:.2f} VND")
elif chon == "2":
    m3 = float(input("Nhap so m3 nuoc: "))
    tien = m3 * 8000
    print(f"Tien nuoc: {tien:.2f} VND")
else:
    print("Lua chon khong hop le")
