# Thong ke doanh thu theo thang (12 thang)
doanh_thu_thang = []
for t in range(1, 13):
    dt = float(input(f"Nhap doanh thu Thang {t}: "))
    doanh_thu_thang.append(dt)

tong_nam = sum(doanh_thu_thang)
tb_thang = tong_nam / 12
max_thang = max(doanh_thu_thang)
idx_max = doanh_thu_thang.index(max_thang) + 1

print(f"Tong doanh thu ca nam: {tong_nam:.2f}")
print(f"Doanh thu trung binh moi thang: {tb_thang:.2f}")
print(f"Thang dat doanh thu cao nhat: Thang {idx_max} ({max_thang:.2f})")
