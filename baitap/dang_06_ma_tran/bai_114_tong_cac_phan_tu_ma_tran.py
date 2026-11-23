# Tinh tong cac phan tu trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

tong = 0
for i in range(m):
    for j in range(n):
        val = float(input(f"Nhap phan tu A[{i}][{j}]: "))
        tong += val

print(f"Tong tat ca cac phan tu trong ma tran la: {tong:.2f}")
