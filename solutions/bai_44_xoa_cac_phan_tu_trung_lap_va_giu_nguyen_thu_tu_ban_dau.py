# -*- coding: utf-8 -*-
r"""
Bài 44: Xóa các phần tử trùng lặp và giữ nguyên thứ tự ban đầu
Mức độ: Trung bình
Mục tiêu: Viết chương trình nhập vào một danh sách các số nguyên có thể chứa các phần tử trùng lặp. Hãy loại bỏ các phần tử trùng lặp, chỉ giữ lại lần xuất hiện đầu tiên của mỗi giá trị theo đúng thứ tự xuất hiện ban đầu.
"""

nums = list(map(int, input("Nhập danh sách: ").split()))

unique_list = []
seen = set()

for x in nums:
    if x not in seen:
        unique_list.append(x)
        seen.add(x)

print(" ".join(map(str, unique_list)))
