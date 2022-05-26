lists = ["Elma","Armut",3.14,5,7]
print(lists)
print(len(lists))
#stringler listeye çevrilebilir.
liste2=list("Merhaba")
print(liste2)
print(len(liste2 ))
#liste endeksleri alınabilir
print(lists[2])
#liste parçalama işlemleri
liste3=[1,3,5,7,33,11,44,15,146,19,111]
print(liste3[4:12:3])

#listeler stringler gibi toplanabilir
liste1=[1,3,5]
liste=[100,110,120]
print(liste1+liste)

#listeler değiştirelebilir
liste3[2]=10
print(liste3)#liste3 deki 5 değeri yerine 10 değeri aldı
# """    METODLAR   """

#append metodu
liste3.append(27)#27 değerini liste3 e ekledi
print(liste3)
liste3.append("Python Dili  ")
liste3.append(25)
print(liste3)

#pop metodu silmeye yarıyor
liste3.pop(7)
print(liste3)#liste3 deki 7.değeri sildi
liste3.pop()

#sort metodu listedeki elemanların küçükten büyüğe sıralanmasını sağlar
liste3.sort()
print(liste3)
liste3.sort(reverse= True)#tersten küçükten büyüğe sıralamak için kullanılır
print(liste3)