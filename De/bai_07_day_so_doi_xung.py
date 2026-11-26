# -*- coding: utf-8 -*-
"""
Bài 7. Dãy số đối xứng
Cho mảng số nguyên. Lọc các số có dạng đối xứng (đọc xuôi và ngược giống nhau).
Tìm dãy con liên tiếp có tổng lớn nhất.
"""

def is_palindrome(x):
    if x < 0:
        return False
    s = str(x)
    return s == s[::-1]

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

palindromes = [x for x in nums if is_palindrome(x)]
print(f"Các số đối xứng đã lọc: {palindromes}")

if not palindromes:
    print("Không có số đối xứng nào trong mảng.")
else:
    # Vì các số đối xứng đều >= 0, đoạn con liên tiếp có tổng lớn nhất chính là toàn bộ mảng palindromes
    # Trường hợp tổng quát (áp dụng thuật toán Kadane và truy vết đoạn):
    max_so_far = palindromes[0]
    current_max = palindromes[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(palindromes)):
        if current_max + palindromes[i] > palindromes[i]:
            current_max += palindromes[i]
        else:
            current_max = palindromes[i]
            temp_start = i

        if current_max > max_so_far:
            max_so_far = current_max
            start = temp_start
            end = i

    best_sub = palindromes[start : end + 1]
    print(f"Dãy con liên tiếp có tổng lớn nhất: {best_sub}")
    print(f"Tổng lớn nhất: {max_so_far}")
