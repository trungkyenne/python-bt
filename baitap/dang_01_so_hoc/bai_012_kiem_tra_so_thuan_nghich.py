# Kiem tra so thuan nghich
s = input("Nhap so can kiem tra: ")
if s == s[::-1]:
    print(f"So {s} la so thuan nghich")
else:
    print(f"So {s} khong phai la so thuan nghich")
