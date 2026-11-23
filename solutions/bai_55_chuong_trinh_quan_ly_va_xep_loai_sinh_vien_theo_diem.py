# -*- coding: utf-8 -*-
r"""
Bài 55: Chương trình quản lý và xếp loại sinh viên theo điểm
Mức độ: Trung bình
Mục tiêu: Viết chương trình quản lý thông tin điểm của một lớp gồm $N$ sinh viên. Mỗi sinh viên gồm: Họ tên và Điểm số (thang điểm 10). Chương trình thực hiện:\n1. Nhập danh sách sinh viên.\n2. Xếp loại học lực cho từng sinh viên: Xuất sắc ($\ge 9.0$), Giỏi ($8.0 - 8.9$), Khá ($6.5 - 7.9$), Trung bình ($5.0 - 6.4$), Yếu ($< 5.0$).\n3. Tìm sinh viên có điểm cao nhất.\n4. Tính điểm trung bình của cả lớp.
"""

def xep_loai(diem):
    if diem >= 9.0:
        return "Xuat sac"
    elif diem >= 8.0:
        return "Gioi"
    elif diem >= 6.5:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

n = int(input("Nhập số lượng sinh viên: "))
danh_sach = []
tong_diem = 0

for _ in range(n):
    dong = input("Nhập Họ tên|Điểm: ")
    ten, diem_str = dong.split("|")
    diem = float(diem_str)
    danh_sach.append({"ten": ten.strip(), "diem": diem})
    tong_diem += diem

# In kết quả xếp loại
top_sv = danh_sach[0]
for sv in danh_sach:
    loai = xep_loai(sv["diem"])
    print(f"{sv['ten']} - Diem: {sv['diem']} - Xep loai: {loai}")
    if sv["diem"] > top_sv["diem"]:
        top_sv = sv

dtb_lop = tong_diem / n
print(f"Sinh vien xuat sac nhat: {top_sv['ten']} ({top_sv['diem']})")
print(f"Diem trung binh lop: {dtb_lop:.2f}")
