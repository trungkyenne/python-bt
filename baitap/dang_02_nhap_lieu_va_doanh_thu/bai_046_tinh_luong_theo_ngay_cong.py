# Tinh luong nhan vien theo so ngay cong
ngay_cong = float(input("Nhap so ngay cong lam viec: "))
luong_ngay = float(input("Nhap muc luong co ban moi ngay: "))

if ngay_cong > 22:
    # Vuot tren 22 ngay duoc tinh them 50% thuong chuyen can cho ngay du
    ngay_chuan = 22
    ngay_vuot = ngay_cong - 22
    tong_luong = (ngay_chuan * luong_ngay) + (ngay_vuot * luong_ngay * 1.5)
else:
    tong_luong = ngay_cong * luong_ngay

print(f"Tong tien luong nhan vien: {tong_luong:.2f}")
