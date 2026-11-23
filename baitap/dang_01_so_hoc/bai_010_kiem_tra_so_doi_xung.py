# Kiem tra so doi xung (Palindrome)
n = int(input("Nhap so nguyen n: "))
temp = abs(n)
so_dao = 0
while temp > 0:
    so_dao = so_dao * 10 + temp % 10
    temp //= 10

if so_dao == abs(n):
    print(f"So {n} la so doi xung")
else:
    print(f"So {n} khong phai la so doi xung")
