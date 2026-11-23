# Tinh tong cac so tu 1 den N chia het cho K
n = int(input("Nhap so nguyen duong N: "))
k = int(input("Nhap so nguyen duong K: "))

tong = 0
for i in range(1, n + 1):
    if i % k == 0:
        tong += i
print(f"Tong cac so tu 1 den {n} chia het cho {k} la: {tong}")
