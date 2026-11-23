# Tinh tong chuoi so S = 1 + 1/2 + 1/3 + ... + 1/N
n = int(input("Nhap so nguyen duong n: "))
tong = 0.0
for i in range(1, n + 1):
    tong += 1.0 / i
print(f"Tong chuoi S = 1 + 1/2 + ... + 1/{n} la: {tong:.4f}")
