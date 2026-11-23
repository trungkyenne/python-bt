# Phan tich mot so thanh thua so nguyen to
n = int(input("Nhap so nguyen n: "))
temp = n
print(f"Phan tich {n} thanh thua so nguyen to: ", end="")

i = 2
cac_thua_so = []
while i * i <= temp:
    while temp % i == 0:
        cac_thua_so.append(str(i))
        temp //= i
    i += 1
if temp > 1:
    cac_thua_so.append(str(temp))

print(" x ".join(cac_thua_so))
