# Tinh tong cac phan tu tren duong cheo phu cua ma tran vuong N x N
n = int(input("Nhap cap cua ma tran vuong N: "))
tong_phu = 0.0

for i in range(n):
    for j in range(n):
        val = float(input(f"Nhap A[{i}][{j}]: "))
        if i + j == n - 1:
            tong_phu += val

print(f"Tong duong cheo phu la: {tong_phu:.2f}")
