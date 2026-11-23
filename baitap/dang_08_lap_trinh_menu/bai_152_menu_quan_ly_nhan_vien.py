# Menu quan ly nhan vien
nhan_vien = []
while True:
    print("\n=== MENU QUAN LY NHAN VIEN ===")
    print("1. Them nhan vien")
    print("2. Danh sach va tong quy luong")
    print("3. Thoat")
    chon = input("Nhap lua chon: ")
    if chon == "1":
        ten = input("Nhap ten nhan vien: ")
        luong = float(input("Nhap muc luong: "))
        nhan_vien.append({"ten": ten, "luong": luong})
    elif chon == "2":
        tong_luong = sum(nv["luong"] for nv in nhan_vien)
        for nv in nhan_vien:
            print(f"- {nv['ten']}: {nv['luong']:.2f}")
        print(f"Tong quy luong: {tong_luong:.2f}")
    elif chon == "3":
        break
