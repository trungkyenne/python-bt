# Tim hang co tong lon nhat trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [float(input(f"Nhap A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

max_tong = sum(matrix[0])
hang_max = 0

for i in range(1, m):
    tong = sum(matrix[i])
    if tong > max_tong:
        max_tong = tong
        hang_max = i

print(f"Hang co tong lon nhat la hang {hang_max} voi tong = {max_tong:.2f}")
