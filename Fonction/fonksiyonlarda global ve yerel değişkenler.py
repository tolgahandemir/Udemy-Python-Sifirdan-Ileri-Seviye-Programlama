#yerel değişken
"""def fonction() :
    a = 10 #yerel değişken
    print(a)
fonction()
"""
#global değişken
"""b=15#global değişken fonksiyonun içinde yazmaya gerek yok.
def function():
    print(b)
function()
"""
"""s="Tolgahan"#gene global değişken olduğu için
def fonction() :
    print(s)

fonction()
"""
#globaldeki değişkeni kullanmak için fonksiyonun içine global yazılır
d=12
def fonction() :
    global d
    d = 3
    print(d)
fonction()