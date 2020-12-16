#Örnek 2

a = [1,2,3,4]
try:
    print(a[2])
except IndexError:
    print("O kadar İndex'imiz yok maalesef!")
finally:
    print("Ben her türlü durumda çalışırım.")