# Liet ke day Fibonacci den N
n = int(input("Nhap gia tri N: "))
print(f"Day so Fibonacci nho hon hoac bang {n} la:")
f0, f1 = 0, 1
while f0 <= n:
    print(f0, end=" ")
    f0, f1 = f1, f0 + f1
print()
