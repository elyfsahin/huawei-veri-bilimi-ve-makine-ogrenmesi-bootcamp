def selam_ver():
    print("Merhaba")

selam_ver()

#parametre kullanımı
def selam_ver(isim):
    print(f"Merhaba {isim}")

selam_ver("Elif")

#birden fazla parametre
def selam_ver(isim, selamlama_cumlesi):
    print(isim + " " + selamlama_cumlesi)

selam_ver("Elif", "merhabalar!")

#return kullanımı
def topla(a,b):
    sonuc=a+b
    print(f"Sonuç: {sonuc}")
    return sonuc

toplama_islemi_sonucu=topla(3,8)
print(f"Toplama işlemi sonucu: {toplama_islemi_sonucu}")

def hesapla(x,y):
    toplam = x+y
    carpim = x*y
    return toplam,carpim

hesapla_toplam, hesapla_carpim = hesapla(4,8)
print(f"toplam: {hesapla_toplam}")
print(f"çarpım: {hesapla_carpim}")

def selam(isim, mesaj="merhaba"):
    print(f"{isim} {mesaj}")

selam("elif")
selam("ayşe")
selam("arkadaşlar", "iyi günler")

#keyword argüman
def selam(isim, yas, meslek, c, lr, epoch):
     """
    Docstring
    Description: bu fonksiyon selamlama yapar.
    Input: 
        isim (str): kullanıcının ismi
        yas (int): kullanıcının yaşı
        meslek, 
        c, 
        lr, 
        epoch
    Output: None
    """
     print(isim, yas, meslek, c, lr, epoch)

selam(isim = "kaan", yas = "35", meslek = "mühendis", c = "0.4", lr = "0.001", epoch="1000")

#type hint
def topla(a:int, b:int) -> int:
    return a+b

print(topla(3,4))

#fonksiyon içinde fonksiyon kullanımı
def kare(x):
    kare= x**2 #x*x
    return kare

def yazdir(x):
    print(kare(x))

yazdir(6)





