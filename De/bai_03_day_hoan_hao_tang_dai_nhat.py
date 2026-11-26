# -*- coding: utf-8 -*-
"""
Bài 3. Dãy số hoàn hảo tăng dài nhất
Cho mảng số nguyên dương. Lọc các số hoàn hảo (bằng tổng các ước dương thực sự của nó).
Tìm dãy tăng liên tiếp dài nhất.
"""

def is_perfect_number(x):
    if x <= 1:
        return False
    sum_div = 1
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            sum_div += i
            if i * i != x:
                sum_div += x // i
    return sum_div == x

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

perfects = [x for x in nums if is_perfect_number(x)]
print(f"Các số hoàn hảo đã lọc: {perfects}")

if not perfects:
    print("Không có số hoàn hảo nào trong mảng.")
else:
    best_sub = [perfects[0]]
    curr_sub = [perfects[0]]
    for i in range(1, len(perfects)):
        if perfects[i] > perfects[i - 1]:
            curr_sub.append(perfects[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [perfects[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Độ dài: {len(best_sub)}")
    print(f"Dãy số hoàn hảo tăng liên tiếp dài nhất: {best_sub}")
