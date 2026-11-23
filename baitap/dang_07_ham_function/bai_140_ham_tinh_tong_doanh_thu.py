# Viet ham tinh tong doanh thu
def tinh_tong_doanh_thu(ds_dt):
    return sum(ds_dt)

# Chuong trinh chinh
n = int(input("Nhap so ngay can tinh: "))
ds = [float(input(f"Nhap doanh thu ngay {i + 1}: ")) for i in range(n)]
print(f"Tong doanh thu la: {tinh_tong_doanh_thu(ds):.2f}")
