#elif başka bir koşul varsa yapılır
print("""
Toplama=1
Çıkarma=2
Çarpma=3
Bölme=4
programdan çıkmak için de 5'e basınız..
""")
while True:
    işlem=int(input("İşlem yapıcağınız sayıyı griniz: "))
    if(işlem==1):
        a=float(input("1.Sayıyı Griniz"))
        b=float(input("2.Sayuıyı giriniz"))
        toplam=(a+b)
        print("Saayıların toplamı=",toplam)
    elif(işlem==2):
        a = float(input("1.Sayıyı Griniz"))
        b = float(input("2.Sayuıyı giriniz"))
        çıkar=(a-b)
        print("Sayıların çıkarması = ",çıkar)
    elif(işlem==3):
        a = float(input("1.Sayıyı Griniz"))
        b = float(input("2.Sayuıyı giriniz"))
        carp=a*b
        print("Sayıların çarpımı = ",carp)
    elif(işlem==4):
        a = float(input("1.Sayıyı Griniz"))
        b = float(input("2.Sayuıyı giriniz"))
        böl=a/b
        print("Sayıların bölünmesi =",böl)
    elif(işlem==5):
        print("Programdan Çıkış Yapıldı...")
        break
    else:
        print("Yanlış tuşladınız 1-5 arasında tuşlayın...")

