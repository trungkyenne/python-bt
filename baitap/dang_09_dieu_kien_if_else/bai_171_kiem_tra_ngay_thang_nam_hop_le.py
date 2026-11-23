# Kiem tra ngay thang nam hop le
d = int(input("Nhap ngay: "))
m = int(input("Nhap thang: "))
y = int(input("Nhap nam: "))

if y < 1 or m < 1 or m > 12:
    print("Ngay thang nam khong hop le")
else:
    nhuan = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        max_d = 31
    elif m in [4, 6, 9, 11]:
        max_d = 30
    else:
        max_d = 29 if nhuan else 28
    
    if 1 <= d <= max_d:
        print(f"Ngay {d}/{m}/{y} la hop le")
    else:
        print("Ngay khong hop le")
