# Thay the mot ky tu hoac mot tu trong chuoi
s = input("Nhap chuoi ban dau: ")
tu_cu = input("Nhap tu hoac ky tu can thay the: ")
tu_moi = input("Nhap tu hoac ky tu thay the moi: ")

s_moi = s.replace(tu_cu, tu_moi)
print(f"Chuoi sau khi thay the: {s_moi}")
