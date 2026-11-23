# Tinh tien ban hang sau khi ap dung giam gia
tong_tien = float(input("Nhap tong tien hoa don truoc giam gia: "))
phan_tram_giam = float(input("Nhap phan tram giam gia (%): "))

tien_giam = tong_tien * (phan_tram_giam / 100)
thanh_toan = tong_tien - tien_giam

print(f"So tien duoc giam: {tien_giam:.2f}")
print(f"So tien phai thanh toan: {thanh_toan:.2f}")
