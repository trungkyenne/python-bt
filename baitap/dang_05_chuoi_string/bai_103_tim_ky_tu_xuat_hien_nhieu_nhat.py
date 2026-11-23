# Tim ky tu xuat hien nhieu nhat trong chuoi (khong tinh khoang trang)
s = input("Nhap chuoi: ")
dem = {}
for ch in s:
    if ch != " ":
        dem[ch] = dem.get(ch, 0) + 1

if len(dem) > 0:
    max_count = max(dem.values())
    cac_ky_tu = [k for k, v in dem.items() if v == max_count]
    print(f"Ky tu xuat hien nhieu nhat ({max_count} lan) la: {cac_ky_tu}")
else:
    print("Chuoi khong co ky tu nao hop le")
