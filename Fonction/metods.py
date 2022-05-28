#listelerde metodlar

#insert metodu listede
a = [1,2,3,4,5,6]
a.insert(2,"Tolga")#insert metodu kaçıncı elemana değer ya da string eklemek için lkullanılan bire metodtur
print(a)
a.append("Demir")#append metdou sonuna ekler
print(a)
a.pop()#pop metodu eğer içine değer girilmezzsse sondakini listeden çıkarır
print(a)
a.pop(3)#3. değeri çıkardı listeden mesela
print(a)
#eğer metodların ne işlevi yaptığını unutursak help işlemi yapılır
help(a.pop)#indexteki değerleri remove eder
