# Nhan hai ma tran A (M x K) va B (K x N)
m = int(input("Nhap M (so hang ma tran A): "))
k = int(input("Nhap K (so cot A / so hang B): "))
n = int(input("Nhap N (so cot ma tran B): "))

print("--- Nhap ma tran A ---")
a = [[float(input(f"A[{i}][{p}]: ")) for p in range(k)] for i in range(m)]

print("--- Nhap ma tran B ---")
b = [[float(input(f"B[{p}][{j}]: ")) for j in range(n)] for p in range(k)]

c = [[0.0 for _ in range(n)] for _ in range(m)]

for i in range(m):
    for j in range(n):
        for p in range(k):
            c[i][j] += a[i][p] * b[p][j]

print("Ma tran tich C = A x B la:")
for hang in c:
    for val in hang:
        print(f"{val:8.2f}", end=" ")
    print()
