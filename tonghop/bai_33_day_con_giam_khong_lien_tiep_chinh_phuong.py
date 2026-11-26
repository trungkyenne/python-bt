# -*- coding: utf-8 -*-
"""
Bài 33: Tìm dãy con giảm dài nhất không nhất thiết phải liên tiếp (LDS), chỉ xét số chính phương.
"""

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(n**0.5)
    return r * r == n

n = int(input("Nhập số lượng phần tử n: "))
nums = []
for i in range(n):
    nums.append(int(input(f"Nhập phần tử thứ {i + 1}: ")))
squares = [x for x in nums if is_perfect_square(x)]

if not squares:
    print("Không có số chính phương nào trong chuỗi.")
else:
    n = len(squares)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if squares[j] > squares[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                parent[i] = j
                
    max_len = max(dp)
    last_idx = dp.index(max_len)
    
    # Truy vết dãy con giảm
    lds = []
    curr = last_idx
    while curr != -1:
        lds.append(squares[curr])
        curr = parent[curr]
    lds.reverse()
    
    print(f"Các số chính phương được xét: {squares}")
    print(f"Dãy con giảm dài nhất (không nhất thiết liên tiếp): {lds}")
    print(f"Độ dài: {max_len}")
