# -*- coding: utf-8 -*-
"""
Bài 10: Tìm dãy số giảm liên tiếp dài nhất trong chuỗi.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Chuỗi rỗng.")
else:
    longest_sub = [nums[0]]
    curr_sub = [nums[0]]
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            curr_sub.append(nums[i])
        else:
            if len(curr_sub) > len(longest_sub):
                longest_sub = curr_sub
            curr_sub = [nums[i]]
            
    if len(curr_sub) > len(longest_sub):
        longest_sub = curr_sub
        
    print(f"Dãy số giảm liên tiếp dài nhất: {longest_sub}")
    print(f"Độ dài: {len(longest_sub)}")
