# Phan loai tam giac (deu, can, vuong, thuong)
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    eps = 1e-6
    vuong = (abs(a**2 + b**2 - c**2) < eps or 
             abs(a**2 + c**2 - b**2) < eps or 
             abs(b**2 + c**2 - a**2) < eps)
    if a == b == c:
        print("Tam giac deu")
    elif vuong and (a == b or b == c or c == a):
        print("Tam giac vuong can")
    elif vuong:
        print("Tam giac vuong")
    elif a == b or b == c or c == a:
        print("Tam giac can")
    else:
        print("Tam giac thuong")
else:
    print("Khong tao thanh tam giac")
