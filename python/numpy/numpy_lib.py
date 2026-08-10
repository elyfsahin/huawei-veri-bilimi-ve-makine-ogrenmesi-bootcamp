"""

Numpy: Yüksek hızlı sayısal hesap kütüphanesi
    -Büyük veri, hızlı matematik, matris hesaplamaları, bilimsel ve istatiksel işlem
    -Numpy C dili ile yazılmıştır
 
Numpy Neden Gerekli?
    - daha hızlı hesaplama
    - çok boyutlu veri yapıları
        - matrisler, N boyutlu dizi ile, veri tabloları
    - matematiksel işlem kolaylığı

Numpy ve Yapay Zeka
    - scikit-learn (ml)
    - tensorflow ve pytorch (dl)
    - pandas (data science)
"""

import numpy as np

"""
Diziler (array)
    - ndarray: n-dimensional array
"""

#liste ile numpy dizisi arasındaki fark

sayilar=[1,2,3,4,5] #liste
print(sayilar)

dizi=np.array(sayilar) #python listesini numpy arrayine dönüştürdük
print(dizi)

print(type(dizi)) #<class 'numpy.ndarray'>

#numpy dizisi boyutu öğrenme
print(dizi.shape) #(5,) -> 5 elemanlı tek boyutlu

#dizideki verilerin tipi
print(dizi.dtype) #int64

dizi=np.zeros(5) #sıfırlardan oluşan dizi
print(dizi)

dizi=np.ones(5)
print(dizi)

dizi=np.arange(0,10) #belirli aralıkta dizi 
print(dizi)

dizi=np.arange(0,10,2) #belirli aralıklarla dizi
print(dizi)

# belirli bir aralığa eşit bölünmüş diziler
dizi=np.linspace(0,10,5) # 0 ile 10 arasında 5 sayı üret
print(dizi)

##matematiksel işlemler

#toplama: z= a0 + a1w1

a=np.array([1,2,3])
b=np.array([3,4,5])
sonuc=a+b
print(sonuc)

#çıkarma
sonuc=a-b
print(sonuc)

#çarpma
sonuc=a*b
print(sonuc)

#bölme
sonuc=a/b
print(sonuc)

#dizi ile sayı arasında işlem yapma
a=np.array([3,6,9])
sonuc=a*2
print(sonuc)

#dizinin karesini almak
a=np.array([1,2,3,4])
sonuc=a**2
print(sonuc)

#karekökünü alma 
a=np.array([1,4,9,16])
sonuc=np.sqrt(a)
print(sonuc)

#dizinin toplamını bulma
a=np.array([1,2,3,4])
print(np.sum(a))

#ortalamasını bulma
print(np.mean(a))

print(np.max(a))
print(np.min(a))

#standart sapma
print(np.std(a))

##indexing - slicing

#dizilerde indeksleme
dizi=np.array([4,5,6,7,8,9])
print(dizi[0])
print(dizi[3])

#negatif indeksleme
print(dizi[-1]) #son elemanı verir

#slicing: dizi[başlangıç:bitiş]
print(dizi[1:4]) #[5 6 7]
print(dizi[:3]) #[4 5 6]
print(dizi[3:]) #[7 8 9]

#adım(step) kullanımı
print(dizi[::2]) #[4 6 8]
print(dizi[1::3]) #[5 8]

#2 boyutlu dizilerde indeksleme
matris=np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]

    ]
)

print(matris)
print(matris.shape)

print(matris[0,0])

#belirli bir satırı seçmek
print(matris[1, :])

#belirli bir sütunu seçmek
print(matris[:, 2])

#matris dilimleme
print(matris[0:2, 0::])

##dizi birleştirme ve bölme

#dizi birleştirme
a=np.array([1,2,3])
b=np.array([4,5,6])

sonuc=np.concatenate((a,b))
print(sonuc)

#iki boyutlu dizi birleştirme

a=np.array(
    [
        [1,2],
        [3,4]
    ]
)

b=np.array(
    [
        [5,6],
        [7,8]
    ]
)

sonuc=np.concatenate((a,b)) #axis=0 (a,b,axis=0)
print(sonuc)

#axis parametresi
#axis=0 -> satır yönünde birleştirme
#axis=1 -> sütun yönünde birleştirme

sonuc=np.concatenate((a,b), axis=1)
print(sonuc)

# vstack (dikey birleştirme): axis = 0 gibi yapar
sonuc = np.vstack((a, b))
print(sonuc)

# hstack (yatay birleştirme): axis = 1 gibi yapar
sonuc = np.hstack((a, b))
print(sonuc)

#diziyi parçalara bölme
dizi=np.array([1,2,3,4,5,6])

sonuc=np.split(dizi,2) #2 parçaya böl
print(sonuc)

sonuc=np.split(dizi,3) 
print(sonuc)

#2 boyutlu dizilerde bölme
matris = np.array(
    [
        [1, 2],
        [3, 4],
        [5, 6],
        [7, 8]
    ]
)

sonuc=np.split(matris,2) #satır olarak böldü
print(sonuc)

sonuc=np.split(matris,2,axis=1) #sütun olarak
print(sonuc)

##çok boyutlu diziler

#2 boyutlu
matris=np.array(
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]

    ]
)

print(matris)

print(matris.shape) #(3,3) dizinin boyutunu öğrenme
print(matris.ndim)#2 dizinin kaç boyutlu olduğunu öğrenmek
print(matris.size)#9 dizideki eleman sayısı

#3 boyutlu dizi oluşturma

"""
görsel -> (height, width) -> (yükseklik ve genişlik) -> (1920, 1080), (1920, 1080), (1920, 1080), ... (1920, 1080) -> (N, 1920, 1080)

N adet görüntü hepsi 1920 h, 1080 w özelliğine sahip
"""

dizi3=np.array(
    [
       [
           [1,2],
           [3,4]
       ],

       [
           [5,6],
           [7,8]
       ]
    ]
)

print(dizi3)
print(dizi3.shape) #(2,2,2)

# numpy ile çok boyutlu dizi oluşturma (reshape)
dizi = np.arange(12)
print(dizi) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

# matrise dönüştürme
matris = dizi.reshape(3, 4)
print(matris)

matris=dizi.reshape(2,3,2)
print(matris)

# [
#     [
#         [0,1],
#         [2,3],
#         [4,5]
#     ],

#     [
#         [6,7],
#         [8,9],
#         [10,11]
#     ]
# ]


##matris işlemleri

#matris oluşturma
a=np.array(
    [
        [1,2],
        [3,4]
    ]
)

b = np.array([
    [5, 6],
    [7, 8]
]
)

print(a)
print(b)

print(a + b) # toplama
print(a - b) # çıkarma
print(a * b) # çarpma


# gerçek matris çarpımı
sonuc = np.dot(a, b)
print(sonuc)
"""
[1, 2],
[3, 4]
*
[5, 6],
[7, 8]
=
[[19 22]
 [43 50]]
"""

# matris transpose (matrisin ters çevrilmesi)
print(a.T)

"""
[1, 2],
[3, 4]

**satırlar sütun oldu

[[1 3]
 [2 4]]
"""

# matris determinantı
det = np.linalg.det(a)
print(det) # -2.0000000000000004

# matrisin tersi
ters = np.linalg.inv(a)
print(ters)
"""
[[-2.   1. ]
 [ 1.5 -0.5]]
"""

##rastgele sayı üretme

#rastgele ondalık sayılar üretme [0-1] arasında
rastgele=np.random.rand(5)
print(rastgele) #[0.98859414 0.32029012 0.47039623 0.38695996 0.23083679]

rastgele=np.random.rand(3,3)
print(rastgele) # [[0.13375615 0.93672892 0.67278749]
                #  [0.54663513 0.95893291 0.27723936]
                #  [0.59320802 0.44705114 0.18031642]]

# rastgele tam sayı üretme
rastgele = np.random.randint(1, 10, 5) # 1 ile 10 arasında 5 adet rastgele tam sayı üret
print(rastgele) #[2 6 2 7 5]

# rastgele tam sayı matrisi üretme
rastgele = np.random.randint(1, 20, (3, 4)) # 1 ile 20 arasında 3 satır 4 sütun dan oluşan 12 tane tam sayı üret
print(rastgele) #[[11  9 11 14]
                # [14  3 14  4]
                # [13 17  4 13]]

# aynı rastgele sonucu üretmek için (seed)

np.random.seed(42)
rastgele = np.random.rand(5)
print(rastgele) # [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]

# bir diziden rastgele eleman seçmek
dizi = np.array([10, 20, 30, 40, 50])
secim = np.random.choice(dizi)
print(secim)

# birden fazla eleman seçme 
secim = np.random.choice(dizi, 3)
print(secim)