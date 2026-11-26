# -*- coding: utf-8 -*-
"""
Bài 15. Dãy chính phương tăng và chia hết cho 3
Cho mảng số nguyên. Lọc các số chính phương chia hết cho 3.
Tìm dãy tăng liên tiếp dài nhất.
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

filtered = [x for x in nums if is_perfect_square(x) and x % 3 == 0]
print(f"Các số chính phương chia hết cho 3: {filtered}")

if not filtered:
    print("Không có số chính phương chia hết cho 3 nào trong mảng.")
else:
    best_sub = [filtered[0]]
    curr_sub = [filtered[0]]

    for i in range(1, len(filtered)):
        if filtered[i] > filtered[i - 1]:
            curr_sub.append(filtered[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [filtered[i]]

    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Dãy chính phương tăng chia hết cho 3 dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
