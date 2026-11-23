# Tinh tong cac phan tu tren tung hang cua ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

for i in range(m):
    tong_hang = 0.0
    for j in range(n):
        val = float(input(f"Nhap A[{i}][{j}]: "))
        tong_hang += val
    print(f"Tong hang {i}: {tong_hang:.2f}")
