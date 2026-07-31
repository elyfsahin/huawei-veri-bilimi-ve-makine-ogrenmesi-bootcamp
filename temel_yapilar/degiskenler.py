##Integer 
yas=35
ogrenci_sayisi=45
sicaklik=-3

print("Yaş:",yas)

a=10
b=5
toplam=a+b
print("Toplam:",toplam)
carpma=a*b
print("Çarpım:",carpma)
cikarma=a-b
print("Çıkarma:",cikarma)
bolme=a/b
print("Bölme:",bolme)

urun_sayisi=20
birim_fiyati=12
toplam_fiyat=urun_sayisi*birim_fiyati
print("Ürünlerin toplam değeri:",toplam_fiyat)

# yuzde=int(input("Yüzdeyi giriniz: "))
# zamli_fiyat=birim_fiyati + (birim_fiyati*yuzde/100)
# print("Zamlı fiyat:",zamli_fiyat)

##Float
pi=3.14
sicaklik=36.6
print("Sıcaklık:",sicaklik)

sonuc=0.1+0.2
print("Sonuç:",sonuc)

#round
sonuc_yuvarla=round(sonuc,2)
print("Yuvarlanmış sonuç:",sonuc_yuvarla)

# #kdv (%20) hesaplama
# fiyat=float(input("Fiyat giriniz: "))
# print("Fiyat:",fiyat)
# kdvli_fiyat= fiyat + (fiyat * 20/100)
# print("KDV'li fiyat:",kdvli_fiyat)


##String
isim="Elif"
yas="19"

bilgi= "İsmim " + isim + " ve " + yas + " yaşındayım." #concatenation
print(bilgi)

kardes_sayisi=2
sehir="İstanbul"
bilgi2= "Yaşadığım şehir " +sehir+ " ve " +str(kardes_sayisi) + " kardeşim var." #kardes_sayisi int str fonksiyonu ile int to string yaptık
print(bilgi2)

#string metotları
kelime="pyThON"
print("Kelime:",kelime)
kelime_kucuk=kelime.lower()
print("Küçük harf:",kelime_kucuk)

kelime_uzunluk=len(kelime)
print("Kelimenin uzunluğu:",kelime_uzunluk)

metin="hello"
print(metin.replace("h","H"))


