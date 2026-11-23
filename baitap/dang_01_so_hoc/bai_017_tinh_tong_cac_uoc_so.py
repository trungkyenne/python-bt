# Tinh tong cac uoc so cua N
n = int(input("Nhap so nguyen n: "))
n = abs(n)
tong = 0
for i in range(1, n + 1):
    if n % i == 0:
        tong += i
print(f"Tong cac uoc so cua {n} la: {tong}")
