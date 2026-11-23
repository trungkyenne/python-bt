# Chuyen vi ma tran (Transpose Matrix) M x N thanh N x M
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [input(f"Nhap A[{i}][{j}]: ") for j in range(n)]
    matrix.append(hang)

print("Ma tran chuyen vi la:")
for j in range(n):
    for i in range(m):
        print(f"{matrix[i][j]:>5}", end=" ")
    print()
