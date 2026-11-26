# -*- coding: utf-8 -*-
"""
Bài 22: Tìm dãy số vừa là số chính phương vừa là số nguyên tố.
Ghi chú: Theo toán học, số chính phương n = k^2 (với k >= 0).
Số nguyên tố chỉ chia hết cho 1 và chính nó.
Do đó, không tồn tại số nguyên nào vừa là số chính phương vừa là số nguyên tố.
Chương trình kiểm tra tính chất này trên chuỗi số nhập vào.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(n**0.5)
    return r * r == n

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))

res = [x for x in nums if is_prime(x) and is_perfect_square(x)]

print(f"Các số vừa là số chính phương vừa là số nguyên tố: {res}")
print("(Giải thích: Trong toán học, một số nguyên tố chỉ có 2 ước dương là 1 và chính nó, còn số chính phương k^2 (k > 1) luôn có ít nhất các ước 1, k, k^2 nên không thể là số nguyên tố. Do đó tập kết quả này luôn rỗng).")
