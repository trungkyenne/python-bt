# Dem so luong uoc so cua N
n = int(input("Nhap so nguyen n: "))
n = abs(n)
dem = 0
for i in range(1, n + 1):
    if n % i == 0:
        dem += 1
print(f"So luong uoc so cua {n} la: {dem}")
