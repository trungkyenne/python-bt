# Kiem tra so Fibonacci
k = int(input("Nhap so nguyen k: "))
if k < 0:
    print(f"So {k} khong thuoc day Fibonacci")
elif k in [0, 1]:
    print(f"So {k} thuoc day Fibonacci")
else:
    f0, f1 = 0, 1
    while f1 < k:
        f0, f1 = f1, f0 + f1
    if f1 == k:
        print(f"So {k} thuoc day Fibonacci")
    else:
        print(f"So {k} khong thuoc day Fibonacci")
