# -*- coding: utf-8 -*-
"""
Bài 13. Dãy luân phiên chẵn lẻ
Cho mảng số nguyên. Tìm đoạn liên tiếp dài nhất có các phần tử luân phiên
chẵn, lẻ, chẵn, lẻ hoặc lẻ, chẵn, lẻ, chẵn.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Mảng rỗng.")
else:
    best_sub = [nums[0]]
    curr_sub = [nums[0]]

    for i in range(1, len(nums)):
        # Luân phiên khi một số chẵn và một số lẻ, tức tổng hoặc hiệu số dư chia cho 2 khác 0
        if (nums[i] % 2) != (nums[i - 1] % 2):
            curr_sub.append(nums[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [nums[i]]

    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Đoạn liên tiếp luân phiên chẵn lẻ dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
