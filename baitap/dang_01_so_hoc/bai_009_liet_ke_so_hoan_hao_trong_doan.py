# Liet ke cac so hoan hao trong doan [a, b]
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print(f"Cac so hoan hao trong doan [{a}, {b}] la:")
for num in range(max(2, a), b + 1):
    tong_uoc = 1
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            tong_uoc += i
            if i != num // i:
                tong_uoc += num // i
    if tong_uoc == num:
        print(num, end=" ")
print()
