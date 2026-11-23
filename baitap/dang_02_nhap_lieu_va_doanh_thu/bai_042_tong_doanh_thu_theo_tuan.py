# Tinh tong doanh thu theo tung tuan (moi tuan 7 ngay)
so_tuan = int(input("Nhap so tuan: "))
for t in range(so_tuan):
    print(f"--- Nhap du lieu Tuan {t + 1} ---")
    tong_tuan = 0.0
    for d in range(7):
        tien = float(input(f"Nhap doanh thu ngay {d + 1} cua tuan {t + 1}: "))
        tong_tuan += tien
    print(f"Tong doanh thu Tuan {t + 1} la: {tong_tuan:.2f}")
