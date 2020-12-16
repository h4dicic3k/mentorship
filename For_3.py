tr = "şçöğüİı"
ad = input("Kullanıcı adınızı belirleyin: ")

for karakter in ad:
    if karakter in tr:
        print("Türkçe karakter kullanamazsınız!")
        quit()
print("Kullanıcı adınız başarıyla kaydedildi.")