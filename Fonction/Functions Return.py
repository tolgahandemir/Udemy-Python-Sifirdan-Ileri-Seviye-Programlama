#return parametresi fonksiyonu çağırdığı yere geri döndürür

"""def total(a,b,c) :
    print("totals :",a+b+c)

def double(a) :
    print(" ikiyle çarpımı: ", a*2)

toplam = total(3,4,5)#hata veriyor çünkü total değişkeni hiçbir tipe dönüşmemiş halde(int,float vb)
double(toplam)
type(toplam)
"""

"""def total(a,b,c) :
    return a+b+c
def double(a) :
    return(a*2)
toplam = total(3,4,5)
print(double(toplam))  
"""
def ikiyle_topla(a) :
    print("  1.fonction detected ")
    return a+2
def üçle_çarp(a) :
    print("2. Fonction detected ")
    return a * 3
def dörde_böl(a) :
    print("3.Fonction detected")
    return a / 4
print(dörde_böl(ikiyle_topla(üçle_çarp(5))))
