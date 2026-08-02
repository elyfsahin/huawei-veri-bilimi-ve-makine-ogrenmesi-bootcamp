# ============================================================
# SORU 1
# Bir değişken tanımlayalım: ad = "Kaan", yas = 25, ortalama = 3.45
# Bu değişkenlerin tiplerini type() ile yazdıralım.
# ============================================================

isim="Elif"
yas=19
ortalama=3.59

print(type(isim))
print(type(yas))
print(type(ortalama))

# ============================================================
# SORU 2
# Kullanıcıdan yaş bilgisini input() ile alalım.
# Bu yaşın tipini ekrana basalım ve 5 yıl ekleyip sonucu yazdıralım.
# Not: input() her zaman string döndürür, int'e çevirmeyi unutmayalım.
# ============================================================

yas=int(input("Yaşınızı giriniz:"))
print(type(yas))
print("5 yıl sonra:",yas+5)

# ============================================================
# SORU 3
# Bir ürün fiyatı (float) alalım. %18 KDV hesaplayalım.
# Toplam fiyatı 2 basamak olacak şekilde yazdıralım.
# ============================================================
urun_fiyati=float(input("Ürün fiyatını giriniz:"))
kdvli_fiyat=urun_fiyati + (urun_fiyati * 0.18)
print("KDV'li fiyat:",round(kdvli_fiyat,2))

# ============================================================
# SORU 4
# Bir liste oluşturalım: sayilar = [10, 20, 30, 40, 50]
# - İlk elemanı yazdıralım
# - Son elemanı yazdıralım
# - 2. indexten sona kadar olan parçayı yazdıralım
# - Listeye 60 ekleyelim
# - Listedeki 20 değerini silelim
# ============================================================
sayilar=[10,20,30,40,50]
print("İlk eleman:", sayilar[0])
print("Son eleman:", sayilar[4])
print(sayilar[2:])
sayilar.append(60)
sayilar.remove(20)
print(sayilar)

# ============================================================
# SORU 5
# Bir tuple oluşturalım: koordinat = (12, 34)
# - Tuple içindeki değerleri unpacking ile x ve y değişkenlerine alalım
# - x ve y'yi yazdıralım
# - Tuple'ın değiştirilemediğini göstermek için (yorum satırıyla) örnek verelim
# ============================================================

koordinat=(12,34)
x,y=koordinat
print("x:",x)
print("y:",y)
##koordinat[0]=13 #TypeError: 'tuple' object does not support item assignment

# SORU 6
# Bir sözlük (dictionary) oluşturalım:
# ogrenci = {"isim": "Ayşe", "yas": 22, "bolum": "Yazılım"}
# - Öğrencinin ismini yazdıralım
# - "not" anahtarı ile 90 ekleyelim
# - "yas" değerini 23 yaparak güncelleyelim
# - Tüm anahtarları ve tüm değerleri yazdıralım
# ============================================================

ogrenci={
    "isim":"Ayşe",
    "yas":22,
    "bolum":"Yazılım"
}

print("Öğrencinin ismi:",ogrenci["isim"])
ogrenci["not"]=90
ogrenci["yas"]=23
print("Tüm anahtarlar:",ogrenci.keys())
print("Tüm değerler:",ogrenci.values())

# ============================================================
# SORU 7
# Set oluşturalım ve tekrar edenleri temizleyelim:
# liste = ["Ali", "Ayşe", "Ali", "Mehmet", "Ayşe"]
# - listeyi set'e çevirip benzersiz isimleri yazdıralım
# - benzersiz isim sayısını yazdıralım
# ============================================================

liste=["Ali","Ayşe","Ali","Mehmet","Ayşe"]
benzersiz=set(liste)
print("Benzersiz isimler:",benzersiz)
print("Benzersiz isim sayısı:",len(benzersiz))