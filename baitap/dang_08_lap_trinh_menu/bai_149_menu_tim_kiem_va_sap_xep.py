# Menu tim kiem va sap xep danh sach
n = int(input("Nhap so luong phan tu: "))
ds = [int(input(f"Nhap phan tu {i + 1}: ")) for i in range(n)]

print("\n=== MENU TIM KIEM & SAP XEP ===")
print("1. Sap xep tang dan")
print("2. Sap xep giam dan")
print("3. Tim kiem phan tu")

chon = input("Nhap lua chon: ")
if chon == "1":
    print("Danh sach tang dan:", sorted(ds))
elif chon == "2":
    print("Danh sach giam dan:", sorted(ds, reverse=True))
elif chon == "3":
    k = int(input("Nhap so can tim: "))
    if k in ds:
        print(f"Tim thay {k} tai vi tri dau tien {ds.index(k)}")
    else:
        print(f"Khong tim thay {k}")
