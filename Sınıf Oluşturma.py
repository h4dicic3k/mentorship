class Çalışan():
    print("Yeni bir sınıf oluşturuldu")
    unvan = "Personel"
    mesai = "9 - 18"
    def __init__(self):
        print("Yeni bir çalışan oluşturuldu.")
        self.isim = ""
        self.yetenekler = []
        self.maaş = 1600
        self.günsayısı = 0
    def çalış(self):
        print(self.isim,"Şu anda çalışıyor..")
        self.günsayısı += 1
    def terfi(self):
        self.maaş += 200

ahmet = Çalışan()
ahmet.isim = "ahmet"
ahmet.yetenekler.append("Python kullanır.")

print(ahmet.maaş)

ahmet.çalış()

print("Ahmetin toplam çalıştığı gün sayısı: ",ahmet.günsayısı)

print(ahmet.maaş)
ahmet.terfi()
ahmet.terfi()
print("Ahmet'in mevcut maaşı: ",ahmet.maaş)