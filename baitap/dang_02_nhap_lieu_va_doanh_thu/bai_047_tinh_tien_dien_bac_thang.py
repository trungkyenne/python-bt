# Tinh tien dien sinh hoat theo bac thang
kwh = float(input("Nhap so kWh dien tieu thu: "))

if kwh <= 50:
    tien = kwh * 1678
elif kwh <= 100:
    tien = 50 * 1678 + (kwh - 50) * 1734
elif kwh <= 200:
    tien = 50 * 1678 + 50 * 1734 + (kwh - 100) * 2014
else:
    tien = 50 * 1678 + 50 * 1734 + 100 * 2014 + (kwh - 200) * 2536

vat = tien * 0.08
tong = tien + vat

print(f"Tien dien chua thue: {tien:.2f} VND")
print(f"Thue VAT (8%): {vat:.2f} VND")
print(f"Tong tien phai tra: {tong:.2f} VND")
