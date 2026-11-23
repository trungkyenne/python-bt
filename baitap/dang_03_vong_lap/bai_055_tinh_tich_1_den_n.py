# Tinh tich cac so tu 1 den N (N!)
n = int(input("Nhap so nguyen duong N: "))
tich = 1
for i in range(1, n + 1):
    tich *= i
print(f"Tich cac so tu 1 den {n} la: {tich}")
