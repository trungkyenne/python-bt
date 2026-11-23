# Nhap va in ma tran cap M x N
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = []
    for j in range(n):
        val = int(input(f"Nhap phan tu A[{i}][{j}]: "))
        hang.append(val)
    matrix.append(hang)

print("Ma tran vua nhap la:")
for hang in matrix:
    for val in hang:
        print(f"{val:4d}", end="")
    print()
