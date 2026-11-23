# Quan ly doanh thu nhieu nhan vien
so_nv = int(input("Nhap so luong nhan vien: "))
ds_nv = []

for i in range(so_nv):
    ten = input(f"Nhap ten nhan vien {i + 1}: ")
    dt = float(input(f"Nhap doanh thu cua {ten}: "))
    ds_nv.append({"ten": ten, "doanh_thu": dt})

print("\n--- DANH SACH THUONG DOANH THU ---")
for nv in ds_nv:
    dt = nv["doanh_thu"]
    # Thuong 10% neu doanh thu tren 50 trieu, nguoc lai 5%
    thuong = dt * 0.10 if dt >= 50000000 else dt * 0.05
    print(f"Nhan vien: {nv['ten']} - Doanh thu: {dt:.2f} - Thuong: {thuong:.2f}")

top_nv = max(ds_nv, key=lambda x: x["doanh_thu"])
print(f"\nNhan vien xuat sac nhat: {top_nv['ten']} voi doanh thu {top_nv['doanh_thu']:.2f}")
