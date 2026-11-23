# Tinh tong cac phan tu tren duong cheo chinh cua ma tran vuong N x N
n = int(input("Nhap cap cua ma tran vuong N: "))
tong_chinh = 0.0

for i in range(n):
    for j in range(n):
        val = float(input(f"Nhap A[{i}][{j}]: "))
        if i == j:
            tong_chinh += val

print(f"Tong duong cheo chinh la: {tong_chinh:.2f}")
