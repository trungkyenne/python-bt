# -*- coding: utf-8 -*-
"""
Bài 21. Tìm dãy giảm liên tiếp dài nhất sau khi loại bỏ các số âm.
Cho mảng số nguyên. Loại bỏ các số âm (giữ lại các số >= 0).
Tìm dãy con liên tiếp giảm dần nghiêm ngặt dài nhất.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

non_negative = [x for x in nums if x >= 0]
print(f"Mảng sau khi loại bỏ các số âm: {non_negative}")

if not non_negative:
    print("Không còn phần tử nào trong mảng.")
else:
    best_sub = [non_negative[0]]
    curr_sub = [non_negative[0]]

    for i in range(1, len(non_negative)):
        if non_negative[i] < non_negative[i - 1]:
            curr_sub.append(non_negative[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [non_negative[i]]

    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Dãy giảm liên tiếp dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
