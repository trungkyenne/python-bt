# In tam giac Pascal gom N dong
n = int(input("Nhap so dong cua tam giac Pascal: "))

row = [1]
for i in range(n):
    print(" ".join(map(str, row)))
    next_row = [1]
    for j in range(len(row) - 1):
        next_row.append(row[j] + row[j + 1])
    next_row.append(1)
    row = next_row
