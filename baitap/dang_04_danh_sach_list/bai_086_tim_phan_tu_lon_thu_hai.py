# Tim phan tu lon thu hai trong danh sach
n = int(input("Nhap so luong phan tu: "))
ds = []
for i in range(n):
    ds.append(int(input(f"Nhap phan tu thu {i + 1}: ")))

tap_hop = list(set(ds))
tap_hop.sort(reverse=True)

if len(tap_hop) >= 2:
    print(f"Phan tu lon thu hai la: {tap_hop[1]}")
else:
    print("Khong co phan tu lon thu hai (cac phan tu deu bang nhau hoac mang qua it phan tu)")
