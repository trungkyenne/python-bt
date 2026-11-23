# Kiem tra nam nhuan
nam = int(input("Nhap nam can kiem tra: "))
if (nam % 400 == 0) or (nam % 4 == 0 and nam % 100 != 0):
    print(f"Nam {nam} la nam nhuan")
else:
    print(f"Nam {nam} khong phai la nam nhuan")
