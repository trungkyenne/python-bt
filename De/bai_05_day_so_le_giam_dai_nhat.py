# -*- coding: utf-8 -*-
"""
Bài 5. Dãy số lẻ giảm dài nhất
Cho mảng số nguyên. Lọc các số lẻ. Tìm dãy giảm liên tiếp dài nhất
và tính tổng các phần tử trong dãy đó.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

odds = [x for x in nums if x % 2 != 0]
print(f"Các số lẻ đã lọc: {odds}")

if not odds:
    print("Không có số lẻ nào trong mảng.")
else:
    best_sub = [odds[0]]
    curr_sub = [odds[0]]
    for i in range(1, len(odds)):
        if odds[i] < odds[i - 1]:
            curr_sub.append(odds[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [odds[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Dãy số lẻ giảm liên tiếp dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
    print(f"Tổng các phần tử trong dãy: {sum(best_sub)}")
