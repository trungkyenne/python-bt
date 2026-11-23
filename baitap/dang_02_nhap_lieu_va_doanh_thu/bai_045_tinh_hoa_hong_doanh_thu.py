# Tinh hoa hong nhan vien theo doanh thu
doanh_thu = float(input("Nhap doanh thu dat duoc cua nhan vien: "))

# Doanh thu duoi 20 trieu: 3%
# Tu 20 trieu den 50 trieu: 5%
# Tren 50 trieu: 8%
if doanh_thu < 20000000:
    ty_le = 0.03
elif doanh_thu <= 50000000:
    ty_le = 0.05
else:
    ty_le = 0.08

hoa_hong = doanh_thu * ty_le
print(f"Ty le hoa hong: {ty_le * 100:.0f}%")
print(f"Tien hoa hong nhan vien nhan duoc: {hoa_hong:.2f}")
