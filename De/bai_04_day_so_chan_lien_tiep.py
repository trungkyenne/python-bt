# -*- coding: utf-8 -*-
"""
Bài 4. Dãy số chẵn liên tiếp
Cho mảng số nguyên. Lọc các số chẵn. Tìm đoạn liên tiếp dài nhất có giá trị tăng dần.
Nếu có nhiều đoạn cùng độ dài, in đoạn xuất hiện đầu tiên.
"""

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

evens = [x for x in nums if x % 2 == 0]
print(f"Các số chẵn đã lọc: {evens}")

if not evens:
    print("Không có số chẵn nào trong mảng.")
else:
    best_sub = [evens[0]]
    curr_sub = [evens[0]]
    for i in range(1, len(evens)):
        if evens[i] > evens[i - 1]:
            curr_sub.append(evens[i])
        else:
            # Chọn đoạn đầu tiên nên chỉ cập nhật khi len strictly greater
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [evens[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Đoạn chẵn tăng dần dài nhất xuất hiện đầu tiên: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
