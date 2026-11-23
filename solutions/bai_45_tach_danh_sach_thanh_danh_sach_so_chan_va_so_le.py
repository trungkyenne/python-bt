# -*- coding: utf-8 -*-
r"""
Bài 45: Tách danh sách thành danh sách số chẵn và số lẻ
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên. Hãy tách danh sách ban đầu thành 2 danh sách riêng biệt: một danh sách gồm các số chẵn và một danh sách gồm các số lẻ theo đúng thứ tự xuất hiện. In cả 2 danh sách ra màn hình kèm số lượng phần tử của từng danh sách.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))

ds_chan = []
ds_le = []

for x in nums:
    if x % 2 == 0:
        ds_chan.append(x)
    else:
        ds_le.append(x)

print(f"Danh sach chan ({len(ds_chan)}): {' '.join(map(str, ds_chan))}")
print(f"Danh sach le ({len(ds_le)}): {' '.join(map(str, ds_le))}")
