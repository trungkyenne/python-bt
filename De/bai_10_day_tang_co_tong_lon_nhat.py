# -*- coding: utf-8 -*-
"""
Bài 10. Dãy tăng có tổng lớn nhất
Cho mảng số nguyên. Tìm tất cả các đoạn tăng liên tiếp.
Trong đó, tìm đoạn có tổng lớn nhất và xuất đoạn đó.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Mảng rỗng.")
else:
    increasing_segments = []
    curr_seg = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_seg.append(nums[i])
        else:
            increasing_segments.append(curr_seg)
            curr_seg = [nums[i]]
    increasing_segments.append(curr_seg)

    print("Tất cả các đoạn tăng liên tiếp:")
    for idx, seg in enumerate(increasing_segments, 1):
        print(f"  Đoạn {idx}: {seg} (tổng: {sum(seg)})")

    best_seg = max(increasing_segments, key=sum)
    print(f"\nĐoạn tăng có tổng lớn nhất: {best_seg}")
    print(f"Tổng lớn nhất: {sum(best_seg)}")
