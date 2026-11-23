# Quan ly tien luong nhan vien (luong co ban + phu cap - bao hiem)
so_nv = int(input("Nhap so luong nhan vien: "))
bang_luong = []

for i in range(so_nv):
    ten = input(f"Nhap ten nhan vien {i + 1}: ")
    luong_cb = float(input(f"Nhap luong co ban cua {ten}: "))
    phu_cap = float(input(f"Nhap phu cap cua {ten}: "))
    bao_hiem = luong_cb * 0.105 # Khau tru 10.5% bao hiem
    thuc_linh = luong_cb + phu_cap - bao_hiem
    bang_luong.append({"ten": ten, "thuc_linh": thuc_linh})

print("\n--- BANG LUONG THUC LINH ---")
for nv in bang_luong:
    print(f"{nv['ten']}: {nv['thuc_linh']:.2f} VND")
