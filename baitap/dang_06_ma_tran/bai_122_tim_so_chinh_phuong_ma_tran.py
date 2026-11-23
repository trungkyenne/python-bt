# Tim cac so chinh phuong trong ma tran
def la_cp(num):
    if num < 0:
        return False
    can = int(num**0.5)
    return can * can == num

m = int(input("Nhap so hang M: "))
n = int(input("Nhap so cot N: "))

cp = []
for i in range(m):
    for j in range(n):
        val = int(input(f"Nhap A[{i}][{j}]: "))
        if la_cp(val):
            cp.append(val)

print(f"Cac so chinh phuong trong ma tran la: {cp}")
