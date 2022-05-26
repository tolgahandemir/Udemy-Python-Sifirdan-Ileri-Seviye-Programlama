print("""
************************

Alınan sayıları değiştirme porgramı

************************
""")
a=""
b=""
liste = []
a=int(input("1.Sayıyı Giriniz:"))
b=int(input("2.sayıyı girniz :"))
liste.append(a)
liste.append(b)
liste[0]=b
liste[1]=a
print("1.Sayı: {}\n2.Sayı: {}".format(liste[0],liste[1]))
