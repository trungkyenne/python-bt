# Liet ke cac so nguyen to trong doan [a, b]
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print(f"Cac so nguyen to trong doan [{a}, {b}] la:")
for num in range(a, b + 1):
    if num >= 2:
        la_snt = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                la_snt = False
                break
        if la_snt:
            print(num, end=" ")
print()
