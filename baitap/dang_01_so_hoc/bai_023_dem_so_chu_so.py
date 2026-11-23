# Dem so chu so cua mot so
n = int(input("Nhap so nguyen n: "))
temp = abs(n)
if temp == 0:
    dem = 1
else:
    dem = 0
    while temp > 0:
        dem += 1
        temp //= 10
print(f"So chu so cua {n} la: {dem}")
