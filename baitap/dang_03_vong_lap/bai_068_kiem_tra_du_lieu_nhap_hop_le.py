# Kiem tra du lieu nhap hop le bang vong lap (nhap diem so tu 0 den 10)
while True:
    diem = float(input("Nhap diem thi (tu 0 den 10): "))
    if 0 <= diem <= 10:
        print(f"Diem da nhap hop le: {diem:.2f}")
        break
    else:
        print("Diem khong hop le! Vui long nhap lai.")
