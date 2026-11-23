# Menu quan ly san pham va don hang
kho = {"But": 5000, "Vo": 10000, "Thuoc": 3000}
gio_hang = []

while True:
    print("\n=== MENU BAN HANG ===")
    print("1. Xem bang gia san pham")
    print("2. Mua san pham")
    print("3. Tinh tien va thanh toan")
    print("4. Thoat")
    chon = input("Nhap lua chon: ")
    if chon == "1":
        for sp, gia in kho.items():
            print(f"- {sp}: {gia} VND")
    elif chon == "2":
        sp = input("Nhap ten san pham muon mua: ")
        if sp in kho:
            sl = int(input("Nhap so luong: "))
            gio_hang.append((sp, sl, kho[sp]))
            print(f"Da them {sl} {sp} vao gio hang")
        else:
            print("San pham khong co trong kho")
    elif chon == "3":
        tong = sum(item[1] * item[2] for item in gio_hang)
        print(f"Tong tien thanh toan: {tong} VND")
        gio_hang.clear()
    elif chon == "4":
        break
