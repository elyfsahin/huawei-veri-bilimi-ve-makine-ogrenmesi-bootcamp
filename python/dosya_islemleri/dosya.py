"""
Neden dosya işlemleri yapıyoruz?
    - yapay zeka veriden öğrenir, veriyi python ortamına yüklememiz ve işlememiz lazım bu nedenle dosya işlemlerinin mantığını öğrenicez
"""

#dosya açma ve okuma
#"r" read okuma modu
dosya=open("ornek.txt", "r", encoding="utf-8")
icerik=dosya.read()
print(icerik)
dosya.close()

#satır satır okuma
dosya=open("ornek.txt", "r", encoding="utf-8")

for satir in dosya:
    print(satir.strip())

dosya.close()

#dosya içeriğinin işlenmesi

dosya = open("ornek.txt", "r", encoding="utf-8")
icerik=dosya.read()
dosya.close()

print(icerik)
yeni_icerik=icerik.upper()
print(f"Yeni içerik:\n{yeni_icerik}")

#satır sayısını bulma

dosya= open("ornek.txt", "r", encoding="utf-8")
satirlar=dosya.readlines()
dosya.close()

print(type(satirlar))
print(f"Toplam satır: {len(satirlar)}")

#dosyaya yazma
dosya= open("yeni_dosya.txt", "w", encoding="utf-8")
dosya.write("Merhaba Dünya.\n")
dosya.write("Python öğreniyorum.")
dosya.close()

#oku -> işle -> kaydet
dosya = open("ornek.txt", "r", encoding="utf-8")
icerik = dosya.read()
dosya.close()

yeni_icerik=icerik.upper()

dosya = open("islenmis_ornek.txt", "w", encoding="utf-8")
dosya.write(yeni_icerik)
dosya.close()

#with yapısı
with open("ornek.txt","r", encoding="utf-8") as dosya:
    icerik=dosya.read()
    print("with yapısı:")
    print(icerik)
    #otomatik olarak kendi kapanıyor

with open("with_dosya_yazma.txt", "w", encoding="utf-8") as dosya :
    dosya.write("with ile yazma işlemi gerçekleştirildi.")

