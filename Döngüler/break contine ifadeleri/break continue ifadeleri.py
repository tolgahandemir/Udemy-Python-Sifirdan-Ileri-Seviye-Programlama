#break ifadesi
#eğer iç içe döngü kullanıldıysa sadece içinde bulunduğu blocktaki döngüyü sonlandırır
i =0
while(i<10):
    if(i==5):
        break
    print("i:",i)
    i+=1
#for döngüsünde break
liste = [1,2,3,4,5,6]
for i in liste:
    if(i==5):
        break
    print(i)
#continue ifadesi
liste =list(range(11))
for i in liste:
    if(i==3 or i==5):
        continue
    print("i :  ",i)
#while döngüsünde continue
i=0
while(i<10):
    if(i==2):
        i+=1
        continue
    print(i)
    i += 1
