# -*- coding: utf-8 -*-
"""
Bài 17. Dãy có trung bình lớn nhất
Cho mảng số nguyên. Tìm các đoạn tăng liên tiếp có ít nhất 3 phần tử.
Xuất đoạn có giá trị trung bình cộng lớn nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

valid_segments = []
n_len = len(nums)

# Tìm tất cả các đoạn con liên tiếp tăng có ít nhất 3 phần tử
for i in range(n_len):
    curr = [nums[i]]
    for j in range(i + 1, n_len):
        if nums[j] > nums[j - 1]:
            curr.append(nums[j])
            if len(curr) >= 3:
                valid_segments.append(list(curr))
        else:
            break

if not valid_segments:
    print("Không có đoạn tăng liên tiếp nào có ít nhất 3 phần tử.")
else:
    best_seg = max(valid_segments, key=lambda seg: sum(seg) / len(seg))
    best_avg = sum(best_seg) / len(best_seg)
    print(f"Đoạn tăng liên tiếp (>= 3 phần tử) có trung bình lớn nhất: {best_seg}")
    print(f"Độ dài: {len(best_seg)}")
    print(f"Giá trị trung bình cộng: {best_avg:.2f}")
