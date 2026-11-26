# -*- coding: utf-8 -*-
"""
Bài 36: Tìm dãy con tăng dài nhất, trong đó số lượng số chẵn bằng số lượng số lẻ.
(Xét dãy con liên tiếp tăng).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

best_sub = []
n = len(nums)

for i in range(n):
    curr = [nums[i]]
    even_count = 1 if nums[i] % 2 == 0 else 0
    odd_count = 1 if nums[i] % 2 != 0 else 0
    
    for j in range(i + 1, n):
        if nums[j] > nums[j - 1]:
            curr.append(nums[j])
            if nums[j] % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
            if even_count == odd_count and len(curr) > len(best_sub):
                best_sub = list(curr)
        else:
            break

if best_sub:
    print(f"Dãy con tăng dài nhất có số chẵn bằng số lẻ: {best_sub}")
    print(f"Độ dài: {len(best_sub)} (gồm {len(best_sub)//2} số chẵn và {len(best_sub)//2} số lẻ)")
else:
    print("Không tìm thấy dãy con tăng nào có số lượng chẵn bằng số lượng lẻ.")
