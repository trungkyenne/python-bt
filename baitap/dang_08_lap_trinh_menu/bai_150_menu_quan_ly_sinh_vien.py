# Menu quan ly thong tin sinh vien
sinh_vien = []
while True:
    print("\n=== MENU QUAN LY SINH VIEN ===")
    print("1. Them sinh vien")
    print("2. Xem danh sach sinh vien")
    print("3. Thoat")
    chon = input("Nhap lua chon: ")
    if chon == "1":
        ten = input("Nhap ho ten sinh vien: ")
        lop = input("Nhap lop: ")
        sinh_vien.append({"ten": ten, "lop": lop})
        print("Them thanh cong")
    elif chon == "2":
        for i, sv in enumerate(sinh_vien):
            print(f"{i + 1}. Ten: {sv['ten']} - Lop: {sv['lop']}")
    elif chon == "3":
        break
