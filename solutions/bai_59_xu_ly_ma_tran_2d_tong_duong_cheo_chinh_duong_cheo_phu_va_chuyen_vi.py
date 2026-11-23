# -*- coding: utf-8 -*-
r"""
Bài 59: Xử lý ma trận 2D: Tổng đường chéo chính, đường chéo phụ và chuyển vị
Mức độ: Khó
Mục tiêu: Cho một ma trận vuông cấp $N \times N$ gồm các số nguyên. Hãy viết chương trình:\n1. Nhập ma trận từ bàn phím.\n2. Tính tổng các phần tử trên đường chéo chính.\n3. Tính tổng các phần tử trên đường chéo phụ.\n4. In ma trận chuyển vị (Transpose Matrix) của ma trận ban đầu.
"""

n = int(input("Nhập cấp ma trận N: "))
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

sum_chinh = 0
sum_phu = 0

for i in range(n):
    sum_chinh += matrix[i][i]
    sum_phu += matrix[i][n - 1 - i]

print(f"Tong cheo chinh: {sum_chinh}")
print(f"Tong cheo phu: {sum_phu}")
print("Ma tran chuyen vi:")

for j in range(n):
    trans_row = [str(matrix[i][j]) for i in range(n)]
    print(" ".join(trans_row))
