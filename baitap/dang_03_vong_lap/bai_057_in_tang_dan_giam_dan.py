# In cac so tu 1 den N theo thu tu tang dan va giam dan
n = int(input("Nhap so nguyen duong N: "))

print("Thu tu tang dan:")
for i in range(1, n + 1):
    print(i, end=" ")
print()

print("Thu tu giam dan:")
for i in range(n, 0, -1):
    print(i, end=" ")
print()
