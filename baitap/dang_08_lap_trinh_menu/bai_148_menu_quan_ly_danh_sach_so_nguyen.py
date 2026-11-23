# Menu quan ly danh sach so nguyen
ds = []
while True:
    print("\n=== MENU DANH SACH SO NGUYEN ===")
    print("1. Them so vao danh sach")
    print("2. Hien thi danh sach")
    print("3. Tinh tong cac so")
    print("4. Xoa mot so khoi danh sach")
    print("5. Thoat")
    
    chon = input("Nhap lua chon: ")
    if chon == "1":
        x = int(input("Nhap so nguyen can them: "))
        ds.append(x)
    elif chon == "2":
        print(f"Danh sach hien tai: {ds}")
    elif chon == "3":
        print(f"Tong: {sum(ds)}")
    elif chon == "4":
        x = int(input("Nhap so can xoa: "))
        if x in ds:
            ds.remove(x)
            print(f"Da xoa {x}")
        else:
            print("Khong tim thay so can xoa")
    elif chon == "5":
        break
