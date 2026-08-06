# SORU 1
# "notlar.txt" adında bir dosya oluşturun ve içine
# 5 öğrencinin notunu yazın. Her not ayrı satırda olsun.

dosya = open("notlar.txt", "w", encoding="utf-8")
dosya.write("65\n")
dosya.write("85\n")
dosya.write("58\n")
dosya.write("94\n")
dosya.write("75\n")
dosya.close()

# SORU 2
# Bu dosyayı okuyun ve:
# - Notların ortalamasını hesaplayın
# - En yüksek notu bulun
# - En düşük notu bulun

notlar = []
dosya = open("notlar.txt", "r", encoding="utf-8")
for satir in dosya:
    notlar.append(int(satir.strip()))
dosya.close()

ortalama = sum(notlar)/len(notlar)
max_not= max(notlar)
min_not= min(notlar)

print("Notlar: ",notlar)
print("Not ortalaması: ",ortalama)
print("En yüksek not: ",max_not)
print("En düşük not: ",min_not)

# SORU 3
# Eğer ortalama 50'den büyükse "Sınıf geçti"
# değilse "Sınıf kaldı" sonucunu
# "sonuc.txt" dosyasına kaydedin.

dosya = open("sonuc.txt", "w", encoding="utf-8")
dosya.write(f"Ortalama: {ortalama}\n")
if ortalama>50:
    dosya.write("Sonuç: Sınıf geçti.")
else:
    dosya.write("Sonuç: Sınıf kaldı.")
dosya.close()





