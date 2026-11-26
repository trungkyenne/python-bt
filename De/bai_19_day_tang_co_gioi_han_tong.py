# -*- coding: utf-8 -*-
"""
Bài 19. Dãy tăng có giới hạn tổng
Cho mảng số nguyên dương và số nguyên S.
Tìm đoạn tăng liên tiếp dài nhất có tổng không vượt quá S.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
s_limit = int(input("Nhập giá trị S: "))

best_sub = []

for i in range(len(nums)):
    curr = [nums[i]]
    curr_sum = nums[i]
    if curr_sum <= s_limit:
        if len(curr) > len(best_sub):
            best_sub = list(curr)
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[j - 1]:
                if curr_sum + nums[j] <= s_limit:
                    curr.append(nums[j])
                    curr_sum += nums[j]
                    if len(curr) > len(best_sub):
                        best_sub = list(curr)
                else:
                    break
            else:
                break

if best_sub:
    print(f"Đoạn tăng liên tiếp dài nhất có tổng <= {s_limit}: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
    print(f"Tổng: {sum(best_sub)}")
else:
    print(f"Không có đoạn tăng nào có tổng <= {s_limit}.")
