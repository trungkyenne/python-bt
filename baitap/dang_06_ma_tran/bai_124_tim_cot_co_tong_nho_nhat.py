# Tim cot co tong nho nhat trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [float(input(f"Nhap A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

min_tong = sum(matrix[i][0] for i in range(m))
cot_min = 0

for j in range(1, n):
    tong = sum(matrix[i][j] for i in range(m))
    if tong < min_tong:
        min_tong = tong
        cot_min = j

print(f"Cot co tong nho nhat la cot {cot_min} voi tong = {min_tong:.2f}")
