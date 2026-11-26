# -*- coding: utf-8 -*-
"""
Bài 8. Chia dãy theo dấu
Cho mảng số nguyên. Chia mảng thành các đoạn liên tiếp sao cho các phần tử
trong mỗi đoạn cùng dấu. Tìm đoạn có nhiều phần tử nhất.
(Quy ước dấu: số dương (>0), số âm (<0), số 0 coi là một lớp dấu riêng).
"""

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Mảng rỗng.")
else:
    segments = []
    curr_seg = [nums[0]]

    for i in range(1, len(nums)):
        if sign(nums[i]) == sign(nums[i - 1]):
            curr_seg.append(nums[i])
        else:
            segments.append(curr_seg)
            curr_seg = [nums[i]]
    segments.append(curr_seg)

    longest_seg = max(segments, key=len)

    print("Các đoạn cùng dấu được chia:")
    for idx, seg in enumerate(segments, 1):
        print(f"  Đoạn {idx}: {seg} (độ dài: {len(seg)})")

    print(f"\nĐoạn có nhiều phần tử nhất: {longest_seg}")
    print(f"Độ dài: {len(longest_seg)}")
