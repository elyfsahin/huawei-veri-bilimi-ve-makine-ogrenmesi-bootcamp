sayilar=[10,20,30,40]

for s in sayilar:
    print(s+5)

for i in range(5):
    print(i)

toplam=0
for s in sayilar:
    toplam+=s
print("Toplam:",toplam)

sayilar=[1,2,3,4,5,6]

for s in sayilar:
    if s%2==0:
        print(f"Çift: {s}")

kelime="Python"

for harf in kelime:
    print(harf)