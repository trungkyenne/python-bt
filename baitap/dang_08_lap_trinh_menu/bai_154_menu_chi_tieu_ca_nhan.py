# Menu quan ly chi tieu ca nhan
chi_tieu = []
while True:
    print("\n=== MENU QUAN LY CHI TIEU ===")
    print("1. Them khoan chi")
    print("2. Xem danh sach chi tieu")
    print("3. Tong tien da chi")
    print("4. Khoan chi lon nhat")
    print("5. Thoat")
    chon = input("Nhap lua chon: ")
    if chon == "1":
        muc = input("Nhap noi dung chi tieu: ")
        tien = float(input("Nhap so tien: "))
        chi_tieu.append({"muc": muc, "tien": tien})
    elif chon == "2":
        for c in chi_tieu:
            print(f"{c['muc']}: {c['tien']:.2f}")
    elif chon == "3":
        print(f"Tong chi tieu: {sum(c['tien'] for c in chi_tieu):.2f}")
    elif chon == "4":
        if chi_tieu:
            max_c = max(chi_tieu, key=lambda x: x["tien"])
            print(f"Khoan chi lon nhat: {max_c['muc']} ({max_c['tien']:.2f})")
    elif chon == "5":
        break
