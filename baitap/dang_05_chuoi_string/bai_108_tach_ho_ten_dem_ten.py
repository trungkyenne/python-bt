# Tach ho, ten dem va ten tu chuoi ho ten
s = input("Nhap ho ten day du: ")
cac_tu = s.split()

if len(cac_tu) == 1:
    print(f"Ten: {cac_tu[0]}")
elif len(cac_tu) == 2:
    print(f"Ho: {cac_tu[0]}")
    print(f"Ten: {cac_tu[1]}")
else:
    ho = cac_tu[0]
    ten = cac_tu[-1]
    ten_dem = " ".join(cac_tu[1:-1])
    print(f"Ho: {ho}")
    print(f"Ten dem: {ten_dem}")
    print(f"Ten: {ten}")
