# -*- coding: utf-8 -*-
"""
Bài 9. Dãy tăng rồi giảm
Cho mảng số nguyên. Tìm đoạn liên tiếp có dạng tăng dần rồi giảm dần,
trong đó phải có ít nhất một phần tử tăng và một phần tử giảm.
Xuất đoạn dài nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_seg = []

# Duyệt từng đỉnh i (1 <= i <= n-2)
for i in range(1, n - 1):
    # Kiểm tra i có phải là đỉnh (peak) không: nums[i-1] < nums[i] > nums[i+1]
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        left = i - 1
        while left > 0 and nums[left] > nums[left - 1]:
            left -= 1
        right = i + 1
        while right < n - 1 and nums[right] > nums[right + 1]:
            right += 1
        
        curr_seg = nums[left : right + 1]
        if len(curr_seg) > len(best_seg):
            best_seg = curr_seg

if best_seg:
    print(f"Đoạn tăng rồi giảm dài nhất: {best_seg}")
    print(f"Độ dài: {len(best_seg)}")
else:
    print("Không tìm thấy đoạn tăng rồi giảm nào thỏa mãn.")
