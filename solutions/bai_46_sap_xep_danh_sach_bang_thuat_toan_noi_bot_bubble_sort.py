# -*- coding: utf-8 -*-
r"""
Bài 46: Sắp xếp danh sách bằng thuật toán nổi bọt (Bubble Sort)
Mức độ: Khó
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên. Hãy cài đặt thuật toán sắp xếp nổi bọt (Bubble Sort) để sắp xếp danh sách theo thứ tự tăng dần. Yêu cầu: Tự viết thuật toán hai vòng lặp lồng nhau, không sử dụng phương thức `.sort()` hay hàm `sorted()`.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))
n = len(nums)

for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
    if not swapped:
        break

print(" ".join(map(str, nums)))
