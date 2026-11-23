# Tinh luy thua A^B khong su dung toan tu **
a = float(input("Nhap co so a: "))
b = int(input("Nhap so mu b (khong am): "))

ket_qua = 1.0
for _ in range(b):
    ket_qua *= a

print(f"{a}^{b} = {ket_qua}")
