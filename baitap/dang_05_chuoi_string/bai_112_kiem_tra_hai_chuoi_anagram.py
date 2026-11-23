# Kiem tra hai chuoi co phai la dao chu (Anagram) cua nhau khong
s1 = input("Nhap chuoi thu nhat: ")
s2 = input("Nhap chuoi thu hai: ")

clean_s1 = sorted(s1.replace(" ", "").lower())
clean_s2 = sorted(s2.replace(" ", "").lower())

if clean_s1 == clean_s2:
    print("Hai chuoi la Anagram cua nhau (co cung tap hop chu cai)")
else:
    print("Hai chuoi khong phai la Anagram")
