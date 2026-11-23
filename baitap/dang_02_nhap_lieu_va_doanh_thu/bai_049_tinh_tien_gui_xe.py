# Tinh tien gui xe theo thoi gian (gio)
loai_xe = input("Nhap loai xe (xe_may hoac o_to): ").strip().lower()
so_gio = float(input("Nhap so gio gui xe: "))

if loai_xe == "xe_may":
    # 2 gio dau 5000, moi gio tiep theo 2000
    if so_gio <= 2:
        tien = 5000
    else:
        tien = 5000 + (so_gio - 2) * 2000
elif loai_xe == "o_to":
    # 2 gio dau 20000, moi gio tiep theo 10000
    if so_gio <= 2:
        tien = 20000
    else:
        tien = 20000 + (so_gio - 2) * 10000
else:
    tien = 0
    print("Loai xe khong hop le")

if tien > 0:
    print(f"Tien gui xe la: {tien:.2f} VND")
