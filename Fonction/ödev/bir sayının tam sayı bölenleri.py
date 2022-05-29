
def tamsayı_bölenleri(a) :
    tamsayı_bölmesi = []
    for i in range(2,a) :
        if (a % i == 0) :
            tamsayı_bölmesi.append(i)
    return tamsayı_bölmesi
while True :
    sayı= int(input("Sayıyı giriniz : "))
    if(sayı=="q "):
        print("Programdan çıkış yapılıyor ")

    else :
        print("Tam bölenler",tamsayı_bölenleri(sayı))