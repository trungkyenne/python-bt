# Tinh tong cac so tu 1 den N thoa man: la so le va khong chia het cho 3
n = int(input("Nhap so nguyen N: "))
tong = 0
for i in range(1, n + 1):
    if i % 2 != 0 and i % 3 != 0:
        tong += i
print(f"Tong cac so le khong chia het cho 3 tu 1 den {n} la: {tong}")
