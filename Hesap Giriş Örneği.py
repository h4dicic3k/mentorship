kullanici = "hadi1"
sifre = "hadi0"

nickname = input("Kullanıcı adınızı giriniz: ")
parola = input("Parolanızı giriniz: ")
if (kullanici==nickname):
    if (parola==sifre):
        print("Hoşgeldiniz!")
    else:
        print("Parolanızı eksik veya yanlış girdiniz.")
else:
    print("Kullanıcı adınızı eksik veya hatalı girdiniz.")