# 1->Toplama 2->Çıkarma 3->Çarpma 4->Faktöriyel #

import random
import time
import math


skor = 0
while True:
    a = random.randint(1,4)

    print("Lütfen Bekleyin Yeni Soru Hazırlanıyor...")
    time.sleep(2)

    if a == 1:
        print("Toplama işlemi-> ")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("Lütfen",ilksayi,"ile",ikincisayi,"sayılarının toplamını giriniz.")
        sonuc = int(input("Cevap: "))

        if(sonuc==ilksayi+ikincisayi):
            print("Tebrikler,Doğru Bildiniz!")
            skor = skor + 1
            print("Mevcut skorunuz: ",skor)
            time.sleep(2)
        else:
            print("YANLIŞ! Doğru Cevap: ",ilksayi+ikincisayi)
            skor = skor - 3
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
    elif a == 2:
        print("Çıkarma işlemi->")
        ilksayi = random.randint(1,20)
        ikincisayi = random.randint(1,20)
        print("Lütfen",ilksayi,"-",ikincisayi,"işleminin sonucunu giriniz.")
        sonuc = int(input("Cevap: "))

        if(sonuc==ilksayi-ikincisayi):
            print("Tebrikler,Doğru Bildiniz!")
            skor = skor + 1
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
        else:
            print("YANLIŞ! Doğru Cevap: ",ilksayi-ikincisayi)
            skor = skor - 3
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
    elif a== 3:
        print("Çarpma işlemi->")
        ilksayi = random.randint(1,10)
        ikincisayi = random.randint(1,10)
        print("Lütfen", ilksayi, "*", ikincisayi, "işleminin sonucunu giriniz.")
        sonuc = int(input("Cevap: "))

        if (sonuc == ilksayi*ikincisayi):
            print("Tebrikler,Doğru Bildiniz!")
            skor = skor + 1
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
        else:
            print("YANLIŞ! Doğru Cevap: ", ilksayi*ikincisayi)
            skor = skor - 3
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
    elif a==4:
        print("Faktöriyel işlemi->")
        ilksayi = random.randint(1,6)
        print("Lütfen",ilksayi,"sayısının Faktöriyelini hesaplayınız.")
        sonuc = int(input("Cevap: "))

        if(sonuc == math.factorial(ilksayi)):
            print("Tebrikler, Doğru Bildiniz!")
            skor = skor + 1
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)
        else:
            print("YANLIŞ! Doğru Cevap:",math.factorial(ilksayi))
            skor = skor - 3
            print("Mevcut skorunuz: ", skor)
            time.sleep(2)