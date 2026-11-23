# Kiem tra chuoi co phai chuoi con cua chuoi khac
s_me = input("Nhap chuoi me (chuoi goc): ")
s_con = input("Nhap chuoi con can kiem tra: ")

if s_con in s_me:
    print(f"'{s_con}' la chuoi con cua '{s_me}'")
else:
    print(f"'{s_con}' khong phai la chuoi con cua '{s_me}'")
