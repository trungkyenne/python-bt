# Menu thong ke doanh thu theo ngay
n = int(input("Nhap so ngay trong ky thong ke: "))
doanh_thu = [float(input(f"Nhap doanh thu ngay {i + 1}: ")) for i in range(n)]

print("\n=== MENU THONG KE DOANH THU ===")
print("1. Doanh thu cao nhat")
print("2. Doanh thu thap nhat")
print("3. Doanh thu trung binh")

chon = input("Nhap lua chon (1-3): ")
if chon == "1":
    print(f"Doanh thu cao nhat: {max(doanh_thu):.2f}")
elif chon == "2":
    print(f"Doanh thu thap nhat: {min(doanh_thu):.2f}")
elif chon == "3":
    print(f"Doanh thu trung binh: {sum(doanh_thu) / len(doanh_thu):.2f}")
else:
    print("Lua chon khong hop le")
