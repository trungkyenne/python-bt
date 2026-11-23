# Tim vi tri xuat hien cua phan tu X trong ma tran
m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

matrix = []
for i in range(m):
    hang = [int(input(f"Nhap A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

x = int(input("Nhap phan tu X can tim: "))
vi_tri = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == x:
            vi_tri.append((i, j))

if len(vi_tri) > 0:
    print(f"Phan tu {x} xuat hien tai cac toa do (hang, cot):")
    for r, c in vi_tri:
        print(f"({r}, {c})")
else:
    print(f"Phan tu {x} khong xuat hien trong ma tran")
