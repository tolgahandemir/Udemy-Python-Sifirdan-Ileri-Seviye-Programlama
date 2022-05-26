print("""
**********************
En büyük sayıyı bulma
1_sayıları sıralama
2_programdan çıış

*********************

""")

while True:
    işlem = int(input("İşlem yapıcağınız sayıyı giriniz :"))

    if(işlem==1):
        a = int(input("1.sayıyı giriniz : "))
        b = int(input("2.sayıyı giriniz : "))
        c = int(input("3.sayıyı giriniz : "))
        if (a > b and a > c):
            print("En büyük sayı:", a)
        elif (b >a and b > c):
            print("En büyük sayı:", b)
        elif (c > a and c >b):
            print("En büyük sayı : ",c)
        else:
            print("Tüm sayılar birbirine eşittir..")

    elif(işlem==2):
        print("programdan çıkış yapılöıyor")
        break
