def hello() :
    print("Merhaba")
    print("Nasılsınız?")
print(type(hello))#function olduğunu söylüyor

#fonksiyonlarda parametreler ve argümanlar

"""def hello(name) : #name değişkenimiz burada PARAMETREDİR
    print("Name : ",name)
hello("Tolga")#burada içine yazdığımız değer de ARGÜMAN olarak geçer
hello("Ahmet")
hello("Emin")
"""
#Toplama ile alakalı fonksiyon yazalım
"""def addition(a,b,c) :
    print("Numbers total :",(a+b+c))

addition(15,17,35)
"""
#Faktöriyel fonksiyonu oluşturma :
def factoriel(a) :
    factoriell = 1
    for i in range(2,a+1):
        factoriell *= i
    print("Factroiel", factoriell)
factoriel(5)
factoriel(7)
