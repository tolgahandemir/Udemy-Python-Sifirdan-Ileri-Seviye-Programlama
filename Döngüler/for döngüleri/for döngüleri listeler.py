#in operatörü

print("a" in "Merhaba")#açıklaması Merhabanın içinde a harfi var mıdır?

#for döngüleri : listelerin,demetlerin,stringlerin ve sözlüklerin üzerinde gezinmeni sağlar.
#Listeler üzerinde gezinme
liste = [1,2,3,4,5,6,7]
for eleman in liste :
    print("Listenin içindeki sayılarımız ",eleman)
liste = [1,2,3,4,5,6,7]
toplam = 0
for i in liste :
    toplam=i+toplam
    print("Sayıların toplamı",toplam )
print(toplam  )
liste1 = [2,5,7,11,15,33,34,44,46,56,58]
for i in liste1 :
        if (i%2== 0):
            print(i)