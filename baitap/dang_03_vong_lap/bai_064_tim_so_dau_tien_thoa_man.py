# Tim so dau tien trong khoang tu A den B chia het cho ca 7 va 9
a = int(input("Nhap so bat dau A: "))
b = int(input("Nhap so ket thuc B: "))

so_tim_thay = None
for x in range(a, b + 1):
    if x % 7 == 0 and x % 9 == 0:
        so_tim_thay = x
        break

if so_tim_thay is not None:
    print(f"So dau tien chia het cho ca 7 va 9 la: {so_tim_thay}")
else:
    print(f"Khong co so nao trong khoang [{a}, {b}] chia het cho ca 7 va 9")
