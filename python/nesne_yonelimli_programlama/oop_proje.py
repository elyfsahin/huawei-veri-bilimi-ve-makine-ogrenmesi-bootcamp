"""
Veri analizi aracı
    - sayı listesi tutma
    - bu sayıların toplamını hesapla
    - ortalamasını bul
    - en büyük ve en küçük değerleri göster
"""

class VeriAnaliziAraci:
    def __init__(self,veriler):
        self.veriler=veriler #sayı listesi

    def verileri_goster(self):
        print(f"Veriler: {self.veriler}")

    def toplam_hesapla(self):
        toplam=sum(self.veriler)
        print(f"Toplam: {toplam}")

    def ortalama_hesapla(self):
        ortalama=sum(self.veriler)/len(self.veriler)
        print(f"Ortalama: {ortalama}")

    def maksimum_bul(self):
        maxi=max(self.veriler)
        print(f"Maksimum: {maxi}")

    def minimum_bul(self):
        mini=min(self.veriler)
        print(f"Minimum: {mini}")

analiz1= VeriAnaliziAraci([10,20,30,40,50])

analiz1.verileri_goster()
analiz1.toplam_hesapla()
analiz1.ortalama_hesapla()
analiz1.maksimum_bul()
analiz1.minimum_bul()

