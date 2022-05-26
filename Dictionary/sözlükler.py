dictionary={"bir":1,"iki":2,"üç":3,"dört":4,"beş":5}
print(dictionary)
print(dictionary["iki"])#iki değerine karşılık gelen rakamı söyler
#sözlüklere eleman eklenebilir
dictionary["beş"]= 5#burada beş değerine karşılık gelen değeri gösterdi
print(dictionary)
#sözlüklere + değerler eklenebilir
dictionary["beş"] += 2
print(dictionary)

#METODLAR

#keys metodu
dictionary.keys()
print(dictionary.keys())
print(dictionary.keys())#içindeki anahtarları gösterir

#values metodu
print(dictionary.values())#içindeki değrleri gösterir

#items metodu(listenin içinde demetler oluşturur
print(dictionary.items())