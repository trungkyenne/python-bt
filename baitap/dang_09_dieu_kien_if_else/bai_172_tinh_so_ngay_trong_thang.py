# Tinh so ngay trong thang
m = int(input("Nhap thang (1-12): "))
y = int(input("Nhap nam: "))

if 1 <= m <= 12 and y > 0:
    nhuan = (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)
    if m in [1, 3, 5, 7, 8, 10, 12]:
        ngay = 31
    elif m in [4, 6, 9, 11]:
        ngay = 30
    else:
        ngay = 29 if nhuan else 28
    print(f"Thang {m} nam {y} co {ngay} ngay")
else:
    print("Thang hoac nam khong hop le")
