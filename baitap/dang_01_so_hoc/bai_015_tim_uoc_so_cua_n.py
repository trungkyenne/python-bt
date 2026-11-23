# Tim uoc so cua mot so nguyen
n = int(input("Nhap so nguyen n: "))
n = abs(n)
print(f"Cac uoc so nguyen duong cua {n} la:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()
