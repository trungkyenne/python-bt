# -*- coding: utf-8 -*-
"""
Bài 24. Tìm đoạn tăng liên tiếp dài nhất nhưng không chứa số chính phương.
"""

def is_perfect_square(x):
    if x < 0:
        return False
    r = int(x**0.5)
    return r * r == x

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_sub = []
curr_sub = []

for x in nums:
    if not is_perfect_square(x):
        if not curr_sub or x > curr_sub[-1]:
            curr_sub.append(x)
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [x]
    else:
        # Gặp số chính phương thì ngắt đoạn
        if len(curr_sub) > len(best_sub):
            best_sub = curr_sub
        curr_sub = []

if len(curr_sub) > len(best_sub):
    best_sub = curr_sub

if best_sub:
    print(f"Đoạn tăng liên tiếp dài nhất không chứa số chính phương: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
else:
    print("Không tìm thấy đoạn tăng thỏa mãn điều kiện.")
