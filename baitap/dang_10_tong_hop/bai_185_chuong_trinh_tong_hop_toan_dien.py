# Chuong trinh tong hop: Quan ly diem so voi day du ham, vong lap, dieu kien va danh sach
def nhap_danh_sach_diem():
    ds = []
    n = int(input("Nhap so luong sinh vien: "))
    for i in range(n):
        while True:
            diem = float(input(f"Nhap diem cho sinh vien {i + 1} (0-10): "))
            if 0 <= diem <= 10:
                ds.append(diem)
                break
            else:
                print("Diem phai trong khoang 0 den 10! Vui long nhap lai.")
    return ds

def thong_ke(ds):
    if not ds:
        return
    tb = sum(ds) / len(ds)
    so_gioi = sum(1 for d in ds if d >= 8.0)
    so_dat = sum(1 for d in ds if d >= 5.0)
    so_truot = len(ds) - so_dat
    
    print("\n=== KET QUA THONG KE MON HOC ===")
    print(f"So luong sinh vien: {len(ds)}")
    print(f"Diem trung binh ca lop: {tb:.2f}")
    print(f"Diem cao nhat: {max(ds):.2f}")
    print(f"Diem thap nhat: {min(ds):.2f}")
    print(f"So sinh vien dat loai Gioi (>= 8.0): {so_gioi}")
    print(f"So sinh vien Dat (>= 5.0): {so_dat}")
    print(f"So sinh vien Truot (< 5.0): {so_truot}")

# Chuong trinh chinh
diem_lop = nhap_danh_sach_diem()
thong_ke(diem_lop)
