"""def selamla(isim) :
    print("Selam ",isim)
selamla("Tolga")
selamla()#çalışmayacak çünkü içine değer girilmesi lazım
#bundan dolayı da isim değşkenine string olarak tanıtmak lazım
"""
def selamla(isim = "İsimsiz") :
    print("Selam",isim)

selamla()

def bilgilerigöstre(ad="Bİlgi yok",soyad="bilgi yok",numara="bilgi yok ") :
    print("Ad : {}\nSoyad : {}\nNumara : {}".format(ad,soyad,numara))

bilgilerigöstre("Tolgahan","Demir","21003  ")
bilgilerigöstre()

def total(*a) : #"*"=parametresi burada demet(tuple) olarak algılanır ve değerleri tuple olarak yazar ve de sonsuz değer girilebilir.
    print(a)
total(11,12,13,14)#tuple olarak aldı değerleri mesela
def totala(*a) :
    totall=0
    for i in a :
        totall += i
    print(totall)

totala(15,16,17)#tüm değerleri toplamış oldu ve sınırsız sayıda değer girilebilir....
totala(20,25,34.5,50)
def çarpma(*a) :
    totall= 1
    for i in a :

        totall *= i
    print(totall)

çarpma(10,2,3,5,6,7,12)



def ikyi_bölme(*a) :
    totall = 2
    for i in a :
        totall = i/totall
    print(totall)

ikyi_bölme(4,12,16,15)