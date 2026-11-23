# Tim so nguyen to lon nhat, nho nhat trong doan [a, b]
a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

ds_snt = []
for num in range(a, b + 1):
    if num >= 2:
        la_snt = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                la_snt = False
                break
        if la_snt:
            ds_snt.append(num)

if len(ds_snt) > 0:
    print(f"So nguyen to nho nhat: {min(ds_snt)}")
    print(f"So nguyen to lon nhat: {max(ds_snt)}")
else:
    print("Khong co so nguyen to nao trong doan da cho")
