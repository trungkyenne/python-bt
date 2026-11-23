# Viet ham tim ngay co doanh thu cao nhat
def tim_ngay_max_doanh_thu(ds_dt):
    if not ds_dt:
        return None, None
    max_dt = max(ds_dt)
    idx = ds_dt.index(max_dt)
    return idx + 1, max_dt

# Chuong trinh chinh
n = int(input("Nhap so ngay: "))
ds = [float(input(f"Nhap doanh thu ngay {i + 1}: ")) for i in range(n)]
ngay, dt_max = tim_ngay_max_doanh_thu(ds)
print(f"Ngay co doanh thu cao nhat la ngay thu {ngay} voi doanh thu {dt_max:.2f}")
