# Tinh tich cac chu so cua mot so
n = int(input("Nhap so nguyen n: "))
temp = abs(n)
if temp == 0:
    tich = 0
else:
    tich = 1
    while temp > 0:
        tich *= (temp % 10)
        temp //= 10
print(f"Tich cac chu so cua {n} la: {tich}")
