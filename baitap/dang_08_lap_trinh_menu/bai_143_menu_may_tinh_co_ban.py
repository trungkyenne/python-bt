# Menu may tinh co ban: cong, tru, nhan, chia
print("=== MENU MAY TINH CO BAN ===")
print("1. Phep cong (+)")
print("2. Phep tru (-)")
print("3. Phep nhan (*)")
print("4. Phep chia (/)")

chon = input("Nhap lua chon cua ban (1-4): ")
a = float(input("Nhap so thu nhat: "))
b = float(input("Nhap so thu hai: "))

if chon == "1":
    print(f"Ket qua: {a} + {b} = {a + b}")
elif chon == "2":
    print(f"Ket qua: {a} - {b} = {a - b}")
elif chon == "3":
    print(f"Ket qua: {a} * {b} = {a * b}")
elif chon == "4":
    if b != 0:
        print(f"Ket qua: {a} / {b} = {a / b:.2f}")
    else:
        print("Loi: Khong the chia cho so 0")
else:
    print("Lua chon khong hop le")
