# Cong hai ma tran cung cap M x N
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

print("--- Nhap ma tran A ---")
a = [[float(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

print("--- Nhap ma tran B ---")
b = [[float(input(f"B[{i}][{j}]: ")) for j in range(n)] for i in range(m)]

c = [[a[i][j] + b[i][j] for j in range(n)] for i in range(m)]

print("Ma tran tong C = A + B la:")
for hang in c:
    for val in hang:
        print(f"{val:6.2f}", end=" ")
    print()
