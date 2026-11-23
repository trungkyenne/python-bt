# Tinh chu vi va dien tich hinh chu nhat
d = float(input("Nhap chieu dai: "))
r = float(input("Nhap chieu rong: "))

if d > 0 and r > 0:
    print(f"Chu vi: {2 * (d + r):.2f}")
    print(f"Dien tich: {d * r:.2f}")
else:
    print("Kich thuoc phai la so duong")
