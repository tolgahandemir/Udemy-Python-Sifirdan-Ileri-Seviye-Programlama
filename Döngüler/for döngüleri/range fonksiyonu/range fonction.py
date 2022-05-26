#range fonksiyonu
range(0,20)
#printle range fonksiyonunu yazarken başına yıldız koymak lazım
print(*range(0,20 ))
#range fonksiyonunda başlangıç değeri vermen gerekmez
print(*range(15))
#range fonksiyonlarında atlama değeri verilebilir
print(*range(1,100,2))#tüm tek sayıları yazdırdı mesela
#for döngülerinde range kullanımı
liste=[1,2,3,4,5]
for i in liste:
    print(i)
for i in range(1,100):
    print(i)
for i in range(1,15):
    print("* "* i  )