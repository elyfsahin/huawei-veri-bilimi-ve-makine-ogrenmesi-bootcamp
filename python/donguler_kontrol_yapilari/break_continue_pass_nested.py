#break -> döngüyü tamamen durdurmak için kullanılır

for i in range(10):
    if i == 6:
        break
    print(i)

print("*"*20)

#continue -> o anki tur atlanır ama döngü devam eder

for i in range(7):
    if i==2:
        continue
    print(i)

#pass -> program hata vermeden boş bir kod bloğu oluşturmak için kullanılır

if True:
    #burayı sonra doldur
    pass

for i in range(4):
    if i==3:
        pass
        #todo: burayı sonra doldur
    print(i)

for i in range(5):
    for j in range(4):
        print(f"i: {i}, j: {j}")