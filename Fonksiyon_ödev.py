mevcutTarih = 2020
def kacYasindasın(dogumYili):
    if(dogumYili>0):
        if(dogumYili<mevcutTarih):
            return "Şu anki yaşın: "+str(mevcutTarih-dogumYili)
        else:
            return "Arkadaşlar birileri zaman makinesini bulmuş!"
    else:
        return "Arkadaşlar bu fosili alalım!"
dogumYili = int(input("Doğum yılınızı giriniz: "))
print(kacYasindasın(dogumYili))