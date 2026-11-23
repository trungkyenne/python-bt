# Tim va liet ke cac so nguyen to trong ma tran
def la_snt(num):
    if num < 2:
        return False
    for k in range(2, int(num**0.5) + 1):
        if num % k == 0:
            return False
    return True

m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

snt = []
for i in range(m):
    for j in range(n):
        val = int(input(f"Nhap A[{i}][{j}]: "))
        if la_snt(val):
            snt.append(val)

print(f"Cac so nguyen to trong ma tran la: {snt}")
