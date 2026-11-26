# -*- coding: utf-8 -*-
"""
Bài 26. Tìm hai đoạn tăng liên tiếp dài nhất, không được chồng lấn lên nhau.
Cho mảng số nguyên. Tìm hai đoạn con liên tiếp tăng nghiêm ngặt sao cho
chúng không giao nhau và tổng độ dài của hai đoạn là lớn nhất
(hoặc là 2 đoạn tăng dài nhất lần lượt).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if n == 0:
    print("Mảng rỗng.")
else:
    # Bước 1: Tìm tất cả các đoạn tăng tối đại (maximal increasing segments)
    segments = []
    start = 0
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            segments.append((start, i - 1, nums[start:i]))
            start = i
    segments.append((start, n - 1, nums[start:n]))

    if len(segments) < 2:
        print(f"Chỉ có 1 đoạn tăng duy nhất: {segments[0][2]}")
        print("Không đủ 2 đoạn tăng không chồng lấn riêng biệt.")
    else:
        # Sắp xếp các đoạn theo độ dài giảm dần
        sorted_segs = sorted(segments, key=lambda s: len(s[2]), reverse=True)
        seg1 = sorted_segs[0]
        seg2 = sorted_segs[1]
        print(f"Đoạn tăng 1: {seg1[2]} (vị trí {seg1[0]}..{seg1[1]}, độ dài {len(seg1[2])})")
        print(f"Đoạn tăng 2: {seg2[2]} (vị trí {seg2[0]}..{seg2[1]}, độ dài {len(seg2[2])})")
        print(f"Tổng độ dài 2 đoạn: {len(seg1[2]) + len(seg2[2])}")
