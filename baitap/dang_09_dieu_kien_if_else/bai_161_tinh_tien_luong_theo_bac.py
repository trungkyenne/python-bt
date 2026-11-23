# Tinh tien luong theo bac luong
bac = int(input("Nhap bac luong (1, 2, 3): "))
luong_co_so = 1800000

if bac == 1:
    he_so = 2.34
elif bac == 2:
    he_so = 2.67
elif bac == 3:
    he_so = 3.00
else:
    he_so = 1.0
    print("Bac luong khong ro, tinh he so mac dinh 1.0")

tong_luong = luong_co_so * he_so
print(f"He so: {he_so}, Tong luong: {tong_luong:.2f} VND")
