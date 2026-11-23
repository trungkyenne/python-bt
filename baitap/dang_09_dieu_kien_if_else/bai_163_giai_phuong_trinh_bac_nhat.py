# Giai phuong trinh bac nhat ax + b = 0
a = float(input("Nhap he so a: "))
b = float(input("Nhap he so b: "))

if a == 0:
    if b == 0:
        print("Phuong trinh co vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    x = -b / a
    print(f"Phuong trinh co nghiem duy nhat x = {x:.2f}")
