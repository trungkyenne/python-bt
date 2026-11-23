# Tinh tong cac so le tu 1 den N
n = int(input("Nhap so nguyen duong N: "))
tong_le = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        tong_le += i
print(f"Tong cac so le tu 1 den {n} la: {tong_le}")
