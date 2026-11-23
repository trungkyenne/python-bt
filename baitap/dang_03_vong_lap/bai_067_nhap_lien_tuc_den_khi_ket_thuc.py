# Nhap du lieu lien tuc den khi gap gia tri ket thuc (so 0)
print("Nhap cac so nguyen lien tuc (nhap 0 de ket thuc):")
tong = 0
dem = 0

while True:
    x = int(input("Nhap so: "))
    if x == 0:
        break
    tong += x
    dem += 1

print(f"Da nhap {dem} so. Tong cac so da nhap la: {tong}")
