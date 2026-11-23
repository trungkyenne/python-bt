# Dem so nguyen am va phu am tieng Anh trong chuoi
s = input("Nhap chuoi ky tu: ")
nguyen_am = 0
phu_am = 0
tap_nguyen_am = "aeiou"

for ch in s:
    if ch.isalpha():
        if ch.lower() in tap_nguyen_am:
            nguyen_am += 1
        else:
            phu_am += 1

print(f"So luong nguyen am: {nguyen_am}")
print(f"So luong phu am: {phu_am}")
