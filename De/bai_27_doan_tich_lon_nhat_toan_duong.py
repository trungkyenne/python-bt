# -*- coding: utf-8 -*-
"""
Bài 27. Tìm đoạn có tích các phần tử lớn nhất, với mọi phần tử đều dương.
Cho mảng số nguyên. Xét các đoạn liên tiếp gồm toàn các phần tử dương (> 0),
tìm đoạn có tích các phần tử là lớn nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

positive_segments = []
curr_seg = []

for x in nums:
    if x > 0:
        curr_seg.append(x)
    else:
        if curr_seg:
            positive_segments.append(curr_seg)
            curr_seg = []
if curr_seg:
    positive_segments.append(curr_seg)

if not positive_segments:
    print("Không có phần tử dương nào trong mảng.")
else:
    def product(lst):
        p = 1
        for val in lst:
            p *= val
        return p

    best_seg = max(positive_segments, key=product)
    print(f"Đoạn có tích các phần tử lớn nhất (toàn dương): {best_seg}")
    print(f"Tích lớn nhất: {product(best_seg)}")
