# -*- coding: utf-8 -*-
"""
Bài 29. Tìm đoạn có số lần chuyển đổi giữa tăng và giảm ít nhất.
Một đoạn đơn điệu (chỉ tăng hoặc chỉ giảm) có 0 lần đổi hướng xu hướng.
Mỗi khi xu hướng đổi từ tăng sang giảm hoặc ngược lại tính là 1 lần chuyển đổi.
Chương trình tìm đoạn con dài (có ít nhất 3 phần tử) có số lần chuyển đổi xu hướng ít nhất (0 lần chuyển đổi - đoạn đơn điệu).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if n < 3:
    print(f"Đoạn có số lần chuyển đổi ít nhất (0 lần): {nums}")
else:
    # Tìm đoạn đơn điệu (0 lần chuyển đổi) dài nhất
    # 1. Dãy tăng liên tiếp dài nhất
    inc_best = [nums[0]]
    curr = [nums[0]]
    for i in range(1, n):
        if nums[i] >= nums[i - 1]:
            curr.append(nums[i])
        else:
            if len(curr) > len(inc_best):
                inc_best = curr
            curr = [nums[i]]
    if len(curr) > len(inc_best):
        inc_best = curr

    # 2. Dãy giảm liên tiếp dài nhất
    dec_best = [nums[0]]
    curr = [nums[0]]
    for i in range(1, n):
        if nums[i] <= nums[i - 1]:
            curr.append(nums[i])
        else:
            if len(curr) > len(dec_best):
                dec_best = curr
            curr = [nums[i]]
    if len(curr) > len(dec_best):
        dec_best = curr

    best_monotonic = inc_best if len(inc_best) >= len(dec_best) else dec_best

    print("Đoạn đơn điệu dài nhất có số lần đổi hướng tăng/giảm ít nhất (0 lần):")
    print(f"Đoạn: {best_monotonic}")
    print(f"Độ dài: {len(best_monotonic)}")
    print("Số lần chuyển đổi tăng/giảm: 0")
