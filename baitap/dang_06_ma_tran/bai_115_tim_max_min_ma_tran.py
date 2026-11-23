# Tim phan tu lon nhat va nho nhat trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [float(input(f"A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

max_val = matrix[0][0]
min_val = matrix[0][0]

for hang in matrix:
    for val in hang:
        if val > max_val:
            max_val = val
        if val < min_val:
            min_val = val

print(f"Phan tu lon nhat trong ma tran: {max_val:.2f}")
print(f"Phan tu nho nhat trong ma tran: {min_val:.2f}")
