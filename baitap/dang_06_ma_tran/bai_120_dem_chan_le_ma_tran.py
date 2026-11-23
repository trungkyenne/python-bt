# Dem so luong phan tu chan va le trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

chan = 0
le = 0
for i in range(m):
    for j in range(n):
        val = int(input(f"Nhap A[{i}][{j}]: "))
        if val % 2 == 0:
            chan += 1
        else:
            le += 1

print(f"So luong phan tu chan: {chan}")
print(f"So luong phan tu le: {le}")
