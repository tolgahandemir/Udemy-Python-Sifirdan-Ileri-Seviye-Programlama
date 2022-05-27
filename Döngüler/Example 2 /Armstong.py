number = input("Sayıyı Giriniz :")
toplam = 0
basamak_sayisi = len(number)
counter = 0
numbers = list(number)

if(len(number) < 4):
    for i in numbers:
        toplam += int(i) ** 3

    if(toplam == int(number)):
        print("Armstrong")
    else:
        print("Degil")

elif(len(number) > 3):
    for i in numbers:
        toplam += int(i) ** basamak_sayisi

    if(toplam == int(number)):
        print("Armstrong")
    else:
        print("Degil")
else:
    print("Input empty Değil")


