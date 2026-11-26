# -*- coding: utf-8 -*-
"""
Bài 34: Tìm dãy con tăng dài nhất sao cho tổng các phần tử là số nguyên tố.
(Xét dãy con liên tiếp tăng có tổng là số nguyên tố).
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

# Duyệt tất cả các đoạn con liên tiếp tăng
n = len(nums)
for i in range(n):
    curr = [nums[i]]
    if is_prime(sum(curr)):
        if len(curr) > len(best_sub):
            best_sub = list(curr)
    for j in range(i + 1, n):
        if nums[j] > nums[j - 1]:
            curr.append(nums[j])
            if is_prime(sum(curr)):
                if len(curr) > len(best_sub):
                    best_sub = list(curr)
        else:
            break

if best_sub:
    print(f"Dãy con tăng dài nhất có tổng là số nguyên tố: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
    print(f"Tổng: {sum(best_sub)} (là số nguyên tố)")
else:
    print("Không tìm thấy dãy con tăng nào có tổng là số nguyên tố.")
