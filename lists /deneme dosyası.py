a= ""
liste=[]
while True:
    a=input("Giridceğiniz değeri yazınız")
    for i in a:
        liste.append(a)
        print(liste)
    if(a=="B"):
        print("İşlem sonlandırıldı")
        break

