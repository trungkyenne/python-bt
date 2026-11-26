# -*- coding: utf-8 -*-
"""
Bài 11. Dãy các phần tử khác nhau
Cho mảng số nguyên. Tìm đoạn liên tiếp dài nhất không chứa hai phần tử có giá trị giống nhau.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Mảng rỗng.")
else:
    # Thuật toán hai con trỏ (Sliding Window)
    last_pos = {}
    best_start = 0
    max_len = 0
    start = 0

    for i in range(len(nums)):
        val = nums[i]
        if val in last_pos and last_pos[val] >= start:
            start = last_pos[val] + 1
        last_pos[val] = i
        
        curr_len = i - start + 1
        if curr_len > max_len:
            max_len = curr_len
            best_start = start

    best_sub = nums[best_start : best_start + max_len]
    print(f"Đoạn liên tiếp dài nhất không chứa phần tử trùng lặp: {best_sub}")
    print(f"Độ dài: {max_len}")
