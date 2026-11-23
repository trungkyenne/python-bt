# Tinh tong cac chu so cua mot so
n = int(input("Nhap so nguyen n: "))
temp = abs(n)
tong = 0
while temp > 0:
    tong += temp % 10
    temp //= 10
print(f"Tong cac chu so cua {n} la: {tong}")
