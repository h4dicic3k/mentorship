def topla(x,y):
    z = x+y
    return z
print(topla(65,48))

#Farklı Örnek:
x = 1
def fonks():
    global x
    x = 5
    print("X'in değeri: ",x)
fonks()
print(x)