# -*- coding: utf-8 -*-
"""
Bài 20: Tìm dãy số nguyên tố tăng dài nhất, nếu có nhiều dãy cùng độ dài thì chọn dãy có tổng lớn nhất.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_sub = []
curr_sub = []

def update_best(curr, best):
    if not curr:
        return best
    if not best:
        return curr
    if len(curr) > len(best):
        return curr
    elif len(curr) == len(best):
        if sum(curr) > sum(best):
            return curr
    return best

for x in nums:
    if is_prime(x):
        if not curr_sub or x > curr_sub[-1]:
            curr_sub.append(x)
        else:
            best_sub = update_best(curr_sub, best_sub)
            curr_sub = [x]
    else:
        best_sub = update_best(curr_sub, best_sub)
        curr_sub = []

best_sub = update_best(curr_sub, best_sub)

if best_sub:
    print(f"Dãy số nguyên tố tăng dài nhất (tổng lớn nhất): {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
    print(f"Tổng: {sum(best_sub)}")
else:
    print("Không có dãy số nguyên tố tăng nào.")
