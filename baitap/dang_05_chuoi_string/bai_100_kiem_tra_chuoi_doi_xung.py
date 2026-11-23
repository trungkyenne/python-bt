# Kiem tra chuoi doi xung (Palindrome)
s = input("Nhap chuoi can kiem tra: ")
clean_s = s.replace(" ", "").lower()

if clean_s == clean_s[::-1]:
    print("Chuoi la chuoi doi xung")
else:
    print("Chuoi khong phai la chuoi doi xung")
