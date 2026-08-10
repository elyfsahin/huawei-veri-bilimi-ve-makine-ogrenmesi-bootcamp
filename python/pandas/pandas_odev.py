import pandas as pd

# ÖRNEK VERİ SETİ
# Aşağıdaki veri seti tüm sorular için kullanılacaktır.

veri = {
    "isim": ["Ali", "Ayşe", "Mehmet", "Zeynep", "Ahmet", "Elif"],
    "yas": [25, 30, 28, 35, 22, 27],
    "sehir": ["Ankara", "İstanbul", "Ankara", "İzmir", "Bursa", "İstanbul"],
    "maas": [5000, 7000, 6000, 8000, 4500, 6500]
}

df = pd.DataFrame(veri)

print("VERİ SETİ")
print(df)
print("-" * 50)


# SORU 1
# DataFrame'in ilk 3 satırını gösterin.
print("1.soru: ",df.head(3))

# SORU 2
# DataFrame'deki sütun isimlerini ekrana yazdırın.
print("2.soru: ",df.columns)

# SORU 3
# Sadece "isim" sütununu seçin.
print("3.soru: ",df["isim"])

# SORU 4
# Sadece "isim" ve "maas" sütunlarını birlikte gösterin.
print("4.soru: ",df[["isim","maas"]])

# SORU 5
# Yaşı 28'den büyük olan kişileri filtreleyin.
print("5.soru: ", df[df["yas"]>28])

# SORU 6
# Maaşı 6000'den büyük olan kişilerin sadece isim ve maaş bilgilerini gösterin.
print("6.soru: ", df[df["maas"]>6000][["isim","maas"]])

# SORU 7
# Maaşa göre küçükten büyüğe sıralayın.
print("7.soru: ", df.sort_values("maas"))

# SORU 8
# Maaşa göre büyükten küçüğe sıralayın.
print("8.soru: ", df.sort_values("maas", ascending=False))

# SORU 9
# Şehirlere göre gruplama yapın ve her şehir için ortalama maaşı hesaplayın.
print("9.soru: ", df.groupby("sehir")["maas"].mean())

# SORU 10
# "yillik_maas" adında yeni bir sütun oluşturun.
# Bu sütun maaşın 12 ile çarpılması ile oluşturulacaktır.
df["yillik_maas"]=df["maas"]*12
print("10.soru: ", df)