#Örnek 1

while True:
    sayi = input("Karesini hesaplamak için bir sayı giriniz: ")
    try:
        print(float(sayi)**2)
    except ValueError:
        print("Geçersiz sayı girdiniz!")



