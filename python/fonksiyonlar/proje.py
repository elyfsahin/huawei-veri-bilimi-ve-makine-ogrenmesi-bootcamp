def ortalama_hesapla(vize: float, final:float) -> float:
    ortalama = (vize*0.4) + (final*0.6)
    return ortalama

def harf_notu_hesapla(ortalama: float) -> str:
    if ortalama >= 85:
        return "A"
    elif ortalama >= 70:
        return "B"
    elif ortalama>=60:
        return "C"
    elif ortalama>=50:
        return "D"
    else:
        return "F"

def sonucu_yazdir(isim:str, ortalama:float, harf:str):
    print("------SONUÇ------")
    print(f"Öğrenci: {isim}")
    print(f"Ortalama: {ortalama}")
    print(f"Harf notu: {harf}")


isim=input("İsminizi giriniz: ")
vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))

ortalama= ortalama_hesapla(vize=vize, final=final)
harf= harf_notu_hesapla(ortalama=ortalama)

sonucu_yazdir(isim= isim,ortalama= ortalama,harf= harf)