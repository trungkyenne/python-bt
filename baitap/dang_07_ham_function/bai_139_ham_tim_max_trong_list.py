# Viet ham tim so lon nhat trong danh sach
def tim_max_list(ds):
    if not ds:
        return None
    max_val = ds[0]
    for x in ds[1:]:
        if x > max_val:
            max_val = x
    return max_val

# Chuong trinh chinh
n = int(input("Nhap so luong phan tu: "))
ds = [float(input(f"Nhap phan tu {i + 1}: ")) for i in range(n)]
print(f"Gia tri lon nhat trong danh sach la: {tim_max_list(ds)}")
