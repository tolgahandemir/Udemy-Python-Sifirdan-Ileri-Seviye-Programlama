a=""
liste=[]
while True:
    a=input("Değerleri gir:")
    b = input("Silinecek değeri giriniz")
    for i in a:
        liste.append(a)
        print(liste)
    if(b=="3"):
        b=input("Silinecek değeri giriniz")
        liste.pop(b)
        print("İşleminiz Silinmiştir",b)
        break