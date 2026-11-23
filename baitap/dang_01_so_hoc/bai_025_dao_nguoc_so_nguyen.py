# Dao nguoc mot so nguyen
n = int(input("Nhap so nguyen n: "))
dau = -1 if n < 0 else 1
temp = abs(n)
dao = 0
while temp > 0:
    dao = dao * 10 + temp % 10
    temp //= 10
dao *= dau
print(f"So dao nguoc cua {n} la: {dao}")
