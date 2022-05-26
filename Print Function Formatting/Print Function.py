#print fonksiyonunda bireden fazla değer bastırmak istiyorsan virgul koyman yeterli
print(3,4,5,10,12,15,17)
#\n karakteri alt alta bastırmak için yazılır
print("Merhaba\nTolgahan\nDemir")
#\t karakteri 1 tablık boşluk atarak kullanır
print("HelloWorld\tŞubat\tHaziran")
#sep parametresi şu işlevde kullanılır
print(34,39,41,sep = "/") #kısacası araya bir şeyler yazdırmak için kullanılır
print("Tolga","Han","Demir",sep = "\n")#burada da görüldüğü gibi slash n ile alt alta da yazdırılabilir
#Yıldızlı parametreler her bir karakterin arasına boşluk bırakır.
print(*"Python")
print(*"Python",sep= "/")
#Formatlama
print("{} {} {}".format("Tolga","Han","Demir "))
