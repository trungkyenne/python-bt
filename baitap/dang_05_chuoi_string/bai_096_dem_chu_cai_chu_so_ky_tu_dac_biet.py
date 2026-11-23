# Dem so chu cai, chu so va ky tu dac biet trong chuoi
s = input("Nhap chuoi ky tu: ")
chu_cai = 0
chu_so = 0
dac_biet = 0

for ch in s:
    if ch.isalpha():
        chu_cai += 1
    elif ch.isdigit():
        chu_so += 1
    else:
        dac_biet += 1

print(f"So chu cai: {chu_cai}")
print(f"So chu so: {chu_so}")
print(f"So ky tu dac biet (bao gom ca khoang trang): {dac_biet}")
