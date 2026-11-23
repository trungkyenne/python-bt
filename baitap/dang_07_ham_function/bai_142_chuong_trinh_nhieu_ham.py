# Viet chuong trinh su dung nhieu ham de thong ke danh sach diem so
def nhap_danh_sach(n):
    return [float(input(f"Nhap diem sinh vien {i + 1}: ")) for i in range(n)]

def tinh_trung_binh(ds):
    return sum(ds) / len(ds) if ds else 0.0

def tim_diem_cao_nhat(ds):
    return max(ds) if ds else 0.0

def dem_dat(ds):
    return sum(1 for d in ds if d >= 5.0)

# Chuong trinh chinh
so_sv = int(input("Nhap so luong sinh vien: "))
bang_diem = nhap_danh_sach(so_sv)
print(f"Diem trung binh ca lop: {tinh_trung_binh(bang_diem):.2f}")
print(f"Diem cao nhat: {tim_diem_cao_nhat(bang_diem):.2f}")
print(f"So sinh vien dat (diem >= 5.0): {dem_dat(bang_diem)}")
