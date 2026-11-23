# Tinh tong cac so tu 1 den N
n = int(input("Nhap so nguyen duong N: "))
tong = 0
for i in range(1, n + 1):
    tong += i
print(f"Tong cac so tu 1 den {n} la: {tong}")
