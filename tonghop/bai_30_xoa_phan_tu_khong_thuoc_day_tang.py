# -*- coding: utf-8 -*-
"""
Bài 30: Nhập chuỗi số, tìm dãy tăng dài nhất, xóa các phần tử không thuộc dãy đó.
(Tức chỉ giữ lại dãy số tăng dài nhất).
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

if not nums:
    print("Chuỗi rỗng.")
else:
    longest_start = 0
    longest_len = 1
    
    curr_start = 0
    curr_len = 1
    
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr_len += 1
        else:
            if curr_len > longest_len:
                longest_len = curr_len
                longest_start = curr_start
            curr_start = i
            curr_len = 1
            
    if curr_len > longest_len:
        longest_len = curr_len
        longest_start = curr_start
        
    longest_sub = nums[longest_start : longest_start + longest_len]
    print(f"Dãy số tăng dài nhất: {longest_sub}")
    print(f"Chuỗi sau khi xóa các phần tử không thuộc dãy đó: {' '.join(map(str, longest_sub))}")
