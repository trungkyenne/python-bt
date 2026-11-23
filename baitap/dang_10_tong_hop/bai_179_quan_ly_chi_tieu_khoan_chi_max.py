# Quan ly chi tieu va thong ke khoan chi lon nhat
k = int(input("Nhap so khoan chi tieu trong thang: "))
chi_tieu = []

for i in range(k):
    muc = input(f"Nhap noi dung khoan chi {i + 1}: ")
    tien = float(input(f"Nhap so tien cho '{muc}': "))
    chi_tieu.append({"muc": muc, "tien": tien})

tong_chi = sum(item["tien"] for item in chi_tieu)
max_chi = max(chi_tieu, key=lambda x: x["tien"])

print(f"\nTong chi tieu trong thang: {tong_chi:.2f}")
print(f"Khoan chi ton kem nhat: {max_chi['muc']} voi so tien {max_chi['tien']:.2f}")
