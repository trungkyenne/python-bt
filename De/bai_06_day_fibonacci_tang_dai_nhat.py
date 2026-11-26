# -*- coding: utf-8 -*-
"""
Bài 6. Dãy Fibonacci tăng dài nhất
Cho mảng số nguyên. Lọc những phần tử thuộc dãy Fibonacci.
Tìm dãy con liên tiếp tăng dần dài nhất trong các phần tử đã lọc.
"""

def is_perfect_square(x):
    if x < 0:
        return False
    r = int(x**0.5)
    return r * r == x

def is_fibonacci(x):
    # Một số x >= 0 thuộc dãy Fibonacci khi và chỉ khi 5*x^2 + 4 hoặc 5*x^2 - 4 là số chính phương
    if x < 0:
        return False
    return is_perfect_square(5 * x * x + 4) or is_perfect_square(5 * x * x - 4)

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

fibs = [x for x in nums if is_fibonacci(x)]
print(f"Các số thuộc dãy Fibonacci đã lọc: {fibs}")

if not fibs:
    print("Không có số nào thuộc dãy Fibonacci trong mảng.")
else:
    best_sub = [fibs[0]]
    curr_sub = [fibs[0]]
    for i in range(1, len(fibs)):
        if fibs[i] > fibs[i - 1]:
            curr_sub.append(fibs[i])
        else:
            if len(curr_sub) > len(best_sub):
                best_sub = curr_sub
            curr_sub = [fibs[i]]
    if len(curr_sub) > len(best_sub):
        best_sub = curr_sub

    print(f"Dãy Fibonacci tăng dần liên tiếp dài nhất: {best_sub}")
    print(f"Độ dài: {len(best_sub)}")
