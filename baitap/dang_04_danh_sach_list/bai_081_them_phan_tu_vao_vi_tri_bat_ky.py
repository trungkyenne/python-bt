# Them phan tu vao vi tri bat ky
n = int(input("Nhap so luong phan tu ban dau: "))
ds = []
for i in range(n):
    ds.append(input(f"Nhap phan tu thu {i + 1}: "))

val = input("Nhap gia tri can them: ")
pos = int(input("Nhap vi tri muon chen (0 den N): "))

if 0 <= pos <= len(ds):
    ds.insert(pos, val)
    print(f"Danh sach sau khi chen: {ds}")
else:
    print("Vi tri chen khong hop le")
