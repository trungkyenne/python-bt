# Tim so lon nhat trong 3 so khong dung max()
a = float(input("Nhap so A: "))
b = float(input("Nhap so B: "))
c = float(input("Nhap so C: "))

so_lon_nhat = a
if b > so_lon_nhat:
    so_lon_nhat = b
if c > so_lon_nhat:
    so_lon_nhat = c

print(f"So lon nhat trong 3 so la: {so_lon_nhat:.2f}")
