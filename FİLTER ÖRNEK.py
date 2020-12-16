def teksayi(sayi):
    return sayi%2==1
print(teksayi(2))

def teksayi(sayi):
    return sayi%2==1

liste = range(1,20)

a = list(filter(teksayi,liste))
print(a)

def baslik(kelime):
    return kelime.istitle()
liste2 = ["Python","php","Django","c++","Yozgat"]

b =list(filter(baslik,liste2))

print(b)