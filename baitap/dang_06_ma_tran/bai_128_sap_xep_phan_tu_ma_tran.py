# Sap xep toan bo cac phan tu trong ma tran theo thu tu tang dan
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

ds = []
for i in range(m):
    for j in range(n):
        ds.append(float(input(f"Nhap A[{i}][{j}]: ")))

ds.sort()
print("Ma tran sau khi sap xep tang dan:")
idx = 0
for i in range(m):
    for j in range(n):
        print(f"{ds[idx]:6.2f}", end=" ")
        idx += 1
    print()
