# Kiem tra 3 canh co tao thanh tam giac hop le khong
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("Ba canh tao thanh tam giac hop le")
else:
    print("Khong phai tam giac hop le")
