# Viet ham kiem tra so doi xung
def la_so_doi_xung(n):
    s = str(abs(n))
    return s == s[::-1]

# Chuong trinh chinh
so = int(input("Nhap so can kiem tra: "))
if la_so_doi_xung(so):
    print(f"{so} la so doi xung")
else:
    print(f"{so} khong phai la so doi xung")
