def kare(sayi):
    return sayi*sayi
sayilar = range(1,10)
a = list(map(kare,sayilar))
print(a)
sayilar2 = [1,3,5,7]
b = list(map(str,sayilar2))
print(b)
c = list(map(int,b))
print(c)