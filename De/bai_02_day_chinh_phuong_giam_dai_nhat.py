# -*- coding: utf-8 -*-
"""
Bài 2. Dãy số chính phương giảm dài nhất
Cho mảng số nguyên. Lọc các số chính phương, sau đó tìm dãy con liên tiếp
có các phần tử giảm dần nghiêm ngặt dài nhất.
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

squares = [x for x in nums if is_perfect_square(x)]
print(f"Các số chính phương đã lọc: {squares}")

if not squares:
    print("Không có số chính phương nào trong mảng.")
else:
    best_sub = [squares[0]]
    curr_sub = [squares[0]]
    for i in range(1, len(squares)):
        if squares[i] < squares[i - 1]:
            curr_sub.append(squares[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [squares[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Độ dài: {len(best_sub)}")
    print(f"Dãy số chính phương giảm dần nghiêm ngặt dài nhất: {best_sub}")
