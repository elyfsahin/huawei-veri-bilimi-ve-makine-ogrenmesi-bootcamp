sayi=10
if sayi>0:
    print("Sayı pozitiftir")

sayi=-3
if sayi>0:
    print("Sayı pozitiftir")
else:
    print("Sayı negatiftir")

ogrenci_notu=76
if ogrenci_notu>=90:
    print("Notunuz AA")
elif ogrenci_notu>=80:
    print("Notunuz BB")
elif ogrenci_notu>=70:
    print("Notunuz CC")
elif ogrenci_notu>=60:
    print("Notunuz DD")
else:
    print("Notunuz FF")

yas=21
ogrenci_mi=True

if yas<25 and ogrenci_mi==True:
    print("Öğrenci indiriminden yararlanabilirsiniz")

meyveler=["elma","armut","muz","kiraz"]

if "elma" in meyveler:
    print("Elma bu listede var")
else:
    print("Elma bu listede yok")


urun=input("Bir meyve girin:")
if urun in meyveler:
    print("Bu meyve stokta var")
else:
    print("Bu meyve stokta yok")
