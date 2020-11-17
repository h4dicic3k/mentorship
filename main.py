import sqlite3

okul = sqlite3.connect("schoolinfosystem.db")

if(okul):
    print("Bağlantı Başarılı.")
else:
    print("Bağlantı Başarısız.")

system = okul.cursor()
system.execute('''
CREATE TABLE ogrenciler (
ogr_no INTEGER PRIMARY KEY,
ogr_adi VARCHAR(50),
ogr_sinif INTEGER(2),
ogr_not INTEGER(3) )
''')

system.execute('''
CREATE TABLE dersler (
ders_no INTEGER PRIMARY KEY,
ders_adi VARCHAR(50),
ders_kategori VARCHAR(50) )
''')

system.execute('''
CREATE TABLE devamsızlık (
dev_no INTEGER PRIMARY KEY,
dev_gün VARCHAR(20),
dev_yok VARCHAR(10) )
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Sema YALMAN",9,86)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Oğuzhan YALÇIN",9,100)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Ahmet KOYUN",10,92)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Simge VARLI",10,49)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Gizem GAYE",11,73)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Selçuk BEYDEMİR",11,98)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Murat ATEŞ",12,67)
''')

system.execute('''
INSERT INTO ogrenciler(ogr_adi,ogr_sinif,ogr_not) VALUES ("Derya DENİZ",12,54)
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("TÜRK DİLİ VE EDEBİYATI","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("DİN KÜLTÜRÜ VE AHLAK BİLGİSİ","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("TARİH","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("COĞRAFYA","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("MATEMATİK","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("FİZİK","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("KİMYA","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("BİYOLOJİ","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("İNGİLİZCE","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("ALMANCA","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("BEDEN EĞİTİMİ VE SPOR","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("MÜZİK","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("SAĞLIK BİLGİSİ VE TRAFİK KÜLTÜRÜ","Ana")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("BİLGİSAYAR BİLİMİ","Seçmeli")
''')

system.execute('''
INSERT INTO dersler(ders_adi,ders_kategori) VALUES ("OSMANLI TÜRKÇESİ","Seçmeli")
''')

system.execute('''
INSERT INTO devamsızlık(dev_gün,dev_yok) VALUES ("Pazartesi",1)
''')

system.execute('''
INSERT INTO devamsızlık(dev_gün,dev_yok) VALUES ("Salı",0)
''')

system.execute('''
INSERT INTO devamsızlık(dev_gün,dev_yok) VALUES ("Çarşamba",3)
''')

system.execute('''
INSERT INTO devamsızlık(dev_gün,dev_yok) VALUES ("Perşembe",0)
''')

system.execute('''
INSERT INTO devamsızlık(dev_gün,dev_yok) VALUES ("Cuma",0)
''')

okul.commit()
okul.close()
 


