# Menu quan ly doanh thu ban hang
ds_dt = []
while True:
    print("\n=== MENU QUAN LY DOANH THU ===")
    print("1. Them doanh thu mot ngay")
    print("2. Xem danh sach doanh thu")
    print("3. Tinh tong doanh thu")
    print("4. Thoat")
    
    chon = input("Nhap lua chon (1-4): ")
    if chon == "1":
        tien = float(input("Nhap so tien doanh thu: "))
        ds_dt.append(tien)
        print("Da them thanh cong")
    elif chon == "2":
        print(f"Danh sach doanh thu: {ds_dt}")
    elif chon == "3":
        print(f"Tong doanh thu hien tai: {sum(ds_dt):.2f}")
    elif chon == "4":
        print("Tam biet!")
        break
    else:
        print("Lua chon khong hop le")
