# Kiem tra so co cac chu so tang dan hoac giam dan
s = str(abs(int(input("Nhap so nguyen n: "))))

tang_dan = True
giam_dan = True

for i in range(len(s) - 1):
    if s[i] >= s[i+1]:
        tang_dan = False
    if s[i] <= s[i+1]:
        giam_dan = False

if tang_dan:
    print("Cac chu so tang dan")
elif giam_dan:
    print("Cac chu so giam dan")
else:
    print("Cac chu so khong tang dan cung khong giam dan")
