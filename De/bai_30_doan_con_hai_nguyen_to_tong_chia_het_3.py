# -*- coding: utf-8 -*-
"""
Bài 30. Tìm đoạn con liên tiếp dài nhất thỏa mãn đồng thời:
có ít nhất 2 số nguyên tố và tổng chia hết cho 3.
"""

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_sub = []

# Duyệt tất cả các đoạn con liên tiếp
for i in range(len(nums)):
    curr_sum = 0
    prime_count = 0
    for j in range(i, len(nums)):
        curr_sum += nums[j]
        if is_prime(nums[j]):
            prime_count += 1
        
        if prime_count >= 2 and curr_sum % 3 == 0:
            seg_len = j - i + 1
            if seg_len > len(best_sub):
                best_sub = nums[i : j + 1]

if best_sub:
    prime_in_sub = [x for x in best_sub if is_prime(x)]
    print(f"Đoạn con liên tiếp dài nhất thỏa mãn: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
    print(f"Tổng: {sum(best_sub)} (chia hết cho 3)")
    print(f"Số lượng số nguyên tố trong đoạn: {len(prime_in_sub)} ({prime_in_sub})")
else:
    print("Không tìm thấy đoạn con nào thỏa mãn cả hai điều kiện.")
