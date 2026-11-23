# Tim so cuoi cung trong doan [A, B] chia het cho 13
a = int(input("Nhap so bat dau A: "))
b = int(input("Nhap so ket thuc B: "))

so_cuoi = None
for x in range(b, a - 1, -1):
    if x % 13 == 0:
        so_cuoi = x
        break

if so_cuoi is not None:
    print(f"So cuoi cung trong [{a}, {b}] chia het cho 13 la: {so_cuoi}")
else:
    print(f"Khong co so nao chia het cho 13 trong [{a}, {b}]")
