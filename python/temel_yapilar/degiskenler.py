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

##veri tipi kontrolü
x=20
print(type(x))

x="25" #type string
print(type(int(x))) #type dönüşümü (casting)

##listeler
sayilar=[3,4,5,6]
karisik=[1,2,"x","y",3.14]
print("Sayılar:",sayilar)

print(karisik[1])

print(len(sayilar)) 

#slicing
harfler=["a","b","c","d","e","f","g"]
print(harfler[1:4])
print(harfler[:3]) 
print(harfler[4:])        

harfler.append("h") #eleman ekleme
print(harfler)

harfler.insert(1,"x") #belirli bir indexe eleman ekleme
print(harfler)

harfler.remove("h") #eleman silme
print(harfler)

harfler.pop() #son elemanı silme
print(harfler)

harfler.pop(1) #belirli bir indexteki elemanı silme
print(harfler)

##tuple
koordinatlar=(10,20)
print(koordinatlar)
print(koordinatlar[0])

#tek elemanlı tuple
x=(4) #bu ifade x=5 ile aynı, print(type(x)) int sonucu verir
x=(4,) #print(type(x)) = <class 'tuple>

#unpacking
koordinat=(20,30)
x,y=koordinat
print(x)
print(y)

t=(20,20,30,30,30,40)
print(t.count(30))

##dictionary
ogrenci= {
    "isim":"Elif", 
    "yas":19,
    "bolum":"Yazılım"
}

print(ogrenci)
print(ogrenci["isim"])

ogrenci["ortalama"]=3.5
print(ogrenci)

del ogrenci["yas"]
print(ogrenci)

print(ogrenci.keys())
print(ogrenci.values())
print(ogrenci.items())

##set
sayilar={1,1,2,3,4,5}
print(sayilar) #tekrar eden elemanlar set içinde sadece bir kez yer alır
#indeks yoktur

liste=[1,1,2,2,2,3,4]
benzersiz=set(liste)
print(benzersiz)

sayilar.add(6)
print(sayilar)

sayilar.remove(4)
print(sayilar)

a={1,3,5,7}
b={5,7,9,13,14}
print(a.union(b)) #birleşim
print(a.intersection(b)) #kesişim
print(a.difference(b)) #fark
print(b.difference(a)) #fark

"""
liste:
    - sıralıdır, değiştirilebilir, tekrar eden elemanlara izin verir
    - liste = [1, 2, 3]
    - kullanım: eleman sırası önemliyse, veri güncellenecekse
    - numpy arrayin temelini oluşturmaktadır

Tuple:
    - sıralıdır, değiştirilemez, tekrar eden elemanlara izin verir
    - tuple = (1, 2, 3, 4)    
    - kullanım: veri sabit kalacaksa, güvenli yapı gerekiyorsa

dictionary:
    - anahtar-değer (key-value pair)
    - anahtarlar benzersizdir
    - değerler tekrar edebilir
    - değiştirilebilir
    - ogrenci = {"isim":"kaan", "yas": 35}
    - anlamlı veri saklamak, etiketli veri tutmak
    - pandas dataframe temelini oluşturur

Set:
    - sırasızdır, tekrar eden elemanları kabul etmez, değiştirilebilir
    - set = {1, 2, 3, 4}
    - kullanım: tekrar eden değerleri temizlemek için, küme işlemleri yapmak için


"""