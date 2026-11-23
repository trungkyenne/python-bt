# Liet ke cac so chinh phuong trong doan [a, b]
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print(f"Cac so chinh phuong trong doan [{a}, {b}] la:")
for num in range(max(0, a), b + 1):
    can = int(num**0.5)
    if can * can == num:
        print(num, end=" ")
print()
