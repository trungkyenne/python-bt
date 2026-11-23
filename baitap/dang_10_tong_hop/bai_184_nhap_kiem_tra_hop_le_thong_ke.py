# Chuong trinh nhap du lieu tuoi cua nhom nguoi, kiem tra hop le va thong ke
danh_sach_tuoi = []
print("Nhap do tuoi cua tung nguoi (nhap so am de dung):")

while True:
    tuoi = int(input("Nhap tuoi: "))
    if tuoi < 0:
        break
    if 0 <= tuoi <= 120:
        danh_sach_tuoi.append(tuoi)
    else:
        print("Do tuoi khong hop le (phai tu 0 den 120)")

if danh_sach_tuoi:
    print(f"So nguoi da nhap: {len(danh_sach_tuoi)}")
    print(f"Tuoi trung binh: {sum(danh_sach_tuoi) / len(danh_sach_tuoi):.1f}")
    print(f"Nguoi lon tuoi nhat: {max(danh_sach_tuoi)}")
    print(f"Nguoi tre tuoi nhat: {min(danh_sach_tuoi)}")
else:
    print("Chua co du lieu hop le nao")
