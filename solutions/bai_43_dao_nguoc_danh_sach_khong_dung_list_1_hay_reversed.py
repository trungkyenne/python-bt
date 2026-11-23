# -*- coding: utf-8 -*-
r"""
Bài 43: Đảo ngược danh sách không dùng list[::-1] hay reversed()
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên. Hãy đảo ngược thứ tự các phần tử trong danh sách đó bằng cách hoán đổi trực tiếp các phần tử đối xứng hai đầu (kỹ thuật Two Pointers - Hai con trỏ). Không sử dụng cú pháp cắt lát `[::-1]`, hàm `reversed()` hay phương thức `.reverse()`.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))

left = 0
right = len(nums) - 1

while left < right:
    # Hoán đổi hai phần tử
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1

print(" ".join(map(str, nums)))
