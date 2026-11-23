# Tinh tong cac phan tu tren tung cot cua ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [float(input(f"Nhap A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

for j in range(n):
    tong_cot = sum(matrix[i][j] for i in range(m))
    print(f"Tong cot {j}: {tong_cot:.2f}")
