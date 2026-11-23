# Quan ly so luong hang ton kho va canh bao het hang
n = int(input("Nhap so mat hang can kiem tra: "))
kho = []

for i in range(n):
    ten = input(f"Nhap ten mat hang {i + 1}: ")
    ton = int(input(f"Nhap so luong ton cua {ten}: "))
    kho.append((ten, ton))

print("\n--- CANH BAO TON KHO ---")
for ten, ton in kho:
    if ton < 5:
        print(f"CANH BAO: Mat hang '{ten}' chi con {ton} san pham (Can nhap them!)")
    else:
        print(f"Mat hang '{ten}': ton kho on dinh ({ton} san pham)")
