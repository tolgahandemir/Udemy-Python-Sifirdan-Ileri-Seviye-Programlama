print("""
************************
Ad soytad numara programı
kullanıcı eklemek için 1 
programı sonlandırmak için 2 ye basınız...
************************
""")
ad=""
soyad=""
numara=""
kişiler=[]
while True:
    işlem=input("İşlem numarasına basınız:")
    if(işlem=="1"):
        ad=input("Adınızı giriniz:")
        soyad=input("Soyadınız giriniz:")
        numara=input("numaranızı giriniz:")
        bilgiler = [ad,soyad,numara]
        kişiler.append(bilgiler)

        print("Ad : {}\nSoyad :{}\nNumara: {}".format(bilgiler[0],bilgiler[1],bilgiler[2]))
    elif(işlem=="2"):
        print("program sonlandırıldı")
        break
