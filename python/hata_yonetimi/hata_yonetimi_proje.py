"""
Bozuk veri temizleme
veri:
        70
        85
        abc
        90
        50
        hata
        60
Amaç:
    - dosyayı oku
    - sayıya çevrilemeyen satıları atla
    - geçerli notları topla
    - ortalama hesapla
"""

notlar=[]
hata_sayisi=0

with open("notlar.txt", "r", encoding="utf-8") as dosya:
    for satir in dosya:
        try:
            not_degeri=int(satir.strip())
            notlar.append(not_degeri)
        except ValueError:
            print(f"Hatalı veri bulundu: {satir.strip()}")
            hata_sayisi+=1

print(f"Notlar: {notlar}")
print(f"Hata sayısı: {hata_sayisi}")

ortalama= sum(notlar)/len(notlar)
print(f"Ortalama: {ortalama}")