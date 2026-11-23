# Menu may tinh co chuc nang lap lai va thoat chuong trinh
while True:
    print("\n=== MAY TINH DON GIAN ===")
    print("1. Cong hai so")
    print("2. Tru hai so")
    print("3. Thoat chuong trinh")
    chon = input("Nhap lua chon (1-3): ")
    
    if chon == "1":
        a = float(input("Nhap so A: "))
        b = float(input("Nhap so B: "))
        print(f"Ket qua: {a} + {b} = {a + b}")
    elif chon == "2":
        a = float(input("Nhap so A: "))
        b = float(input("Nhap so B: "))
        print(f"Ket qua: {a} - {b} = {a - b}")
    elif chon == "3":
        print("Chuong trinh ket thuc. Tam biet!")
        break
    else:
        print("Lua chon khong hop le, vui long thu lai")
