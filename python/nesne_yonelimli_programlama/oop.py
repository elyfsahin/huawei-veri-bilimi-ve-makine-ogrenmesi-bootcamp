"""
Class neden kullanırız?
    - kodun daha düzenli olması için
    - kod tekrarını azaltır
    - büyük projelerde yönetimi kolaylaştırır
    - scikit learn -> en önemli machine learning kütüphanesi -> LinearRegression() class tanımlamış olur.
"""

class Ogrenci:
    def __init__(self,isim,yas): #self = oluşturulan nesneyi temsil eder, isim ve yaş başlangıç parametrelerimiz
        print(f"Yeni bir öğrenci oluşturuluyor, isim:{isim}, yaş:{yas}")

ogrenci1 = Ogrenci("Ali",20)

"""
Attribute bir class a veya nesneye ait özellikleri temsil eden değişkenlerdir.
yani bir nesnenin verilerini tutan yapılarıdır
Öğrenci:
    - isim, yaş ve bölüm: bunlar öğrencinin attribute larıdır.
"""

class Ogrenci:
    def __init__(self,isim,yas):
        self.isim=isim #isim attribute
        self.yas=yas  #yas attribute

ogrenci1 = Ogrenci("Ali", 22)

print(ogrenci1.isim) #Ali
print(ogrenci1.yas) #22

"""
Metot (method): bir class içerisinde tanımlanan fonksiyonlardır
bir nesnenin yapabileceği işlemleri temsil ederler
"""

class Ogrenci:
    def __init__(self,isim,yas):
        self.isim=isim
        self.yas=yas

    def tanit(self):
        print(f"Merhaba benim adım:{self.isim}")

ogrenci1 = Ogrenci("Elif",19)
ogrenci2 = Ogrenci("Kaan",20)

ogrenci1.tanit()
ogrenci2.tanit()

"""
Object oluşturma ve class kullanımı
    - class: şablon -> araba
    - object (nesne): şablondan üretilen yapı (mercedes, audi)

"""

class Kitap: 
    def __init__(self,ad,yazar,sayfa):
        self.ad=ad
        self.yazar=yazar
        self.sayfa=sayfa

    def bilgi_goster(self):
        print(f"Kitap: {self.ad}")
        print(f"Yazar: {self.yazar}")
        print(f"Sayfa sayısı: {self.sayfa}")

kitap1= Kitap("Gurur ve Önyargı", "Jane Austen", 480)

print(kitap1.bilgi_goster())

# birden fazla obje oluşturma
kitap1 = Kitap("Serenad", "Zülfü  Livaneli", 500)
kitap2 = Kitap("Son Ada", "Zülfü Livaneli", 150)
kitap3 = Kitap("Dorian Gray'in Portesi", "Oscar Wilde", 250)

print(kitap2.ad)
kitap3.bilgi_goster()