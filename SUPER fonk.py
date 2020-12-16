class Personel():
    print("Yeni bir sınıf oluşturuldu.")
    mesai = "9 - 18"
    sirket = "Python ile güzel günler!"

    def __init__(self, isim, maaş, yetenekler, konum):
        print("Yeni bir personel oluşturuldu. İsmi: ", isim)
        self.isim = isim
        self.yetenekler = yetenekler
        self.maaş = maaş
        self.konum = konum
        self.günsayısı = 0

    def çalış(self):
        print(self.isim, "Şu anda çalışıyor.. Toplam çalıştığı gün ise şu oldu: ", self.günsayısı + 1)
        self.günsayısı += 1

    def terfi(self):
        print("Tebrikler!", self.isim, "Terfi aldı! Yeni maaşı ise şu oldu: ", self.maaş + 200)
        self.maaş += 200

    def bilgileriGöster(self):
        print("*" * 45)
        print("Personelin ismi: ", self.isim)
        print("Personelin konumu: ", self.konum)
        print("Personelin yetenekleri: ", self.yetenekler)
        print("Personelin maaşı: ", self.maaş)
        print("Personelin toplam gün sayısı: ", self.günsayısı)
        print("*" * 45)


class Yönetici(Personel):

    def __init__(self,isim,maaş,yetenekler,konum,yönetimbecerisi):
        super().__init__(isim,maaş,yetenekler,konum)
        self.yönetimbecerisi = yönetimbecerisi

    def terfi(self):
        print("Tebrikler!", self.isim, "terfi aldı! Yeni maaşı ise şu oldu: ", self.maaş + 500)
        self.maaş += 500

    def gezinti(self):
        print(self.isim, "adlı yönetici şu anda şube gezisine çıkmış bulunmaktadır.")

    def bilgileriGöster(self):
        super().bilgileriGöster()
        print("Yöneticinin Yönetim Becerisi: ", self.yönetimbecerisi)
        print("*"*45)
    def çalış(self):
        super().çalış()
        self.yönetimbecerisi += 0.5
        print("Mevcut Yönetim becerisi: ",self.yönetimbecerisi)

mustafa = Yönetici("Mustafa", 6550, ["İyi yönetir."], "Yönetici",30)
ahmet = Personel("Ahmet", 1600, ["Python kullanır."], "Masabaşı Personeli")
mustafa.çalış()
mustafa.çalış()
mustafa.çalış()