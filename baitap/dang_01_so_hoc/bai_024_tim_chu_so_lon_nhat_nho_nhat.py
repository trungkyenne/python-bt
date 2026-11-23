# Tim chu so lon nhat va nho nhat cua mot so
n = int(input("Nhap so nguyen n: "))
chu_so = [int(c) for c in str(abs(n))]
cs_max = max(chu_so)
cs_min = min(chu_so)

print(f"Chu so lon nhat cua {n} la: {cs_max}")
print(f"Chu so nho nhat cua {n} la: {cs_min}")
