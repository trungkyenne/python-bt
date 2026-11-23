# Dem so tu bat dau bang nguyen am (a, e, i, o, u)
s = input("Nhap chuoi van ban: ")
cac_tu = s.split()
vowels = "aeiou"

dem = 0
for tu in cac_tu:
    if tu[0].lower() in vowels:
        dem += 1

print(f"So tu bat dau bang nguyen am la: {dem}")
