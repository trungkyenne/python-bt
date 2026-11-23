# Kiem tra ma tran vuong N x N co doi xung qua duong cheo chinh khong (A[i][j] == A[j][i])
n = int(input("Nhap cap cua ma tran vuong N: "))

matrix = []
for i in range(n):
    hang = [float(input(f"Nhap A[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

doi_xung = True
for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != matrix[j][i]:
            doi_xung = False
            break
    if not doi_xung:
        break

if doi_xung:
    print("Ma tran la doi xung")
else:
    print("Ma tran khong doi xung")
