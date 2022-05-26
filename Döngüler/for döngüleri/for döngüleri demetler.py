#for döngülerinde demetler
demet = (1,2,3,4,5)
for i in demet:
    print(i)
#liste içinde demetler
liste=[(1,2),(3,4),(5,6),(7,8)]
for i in liste:
    print(i)
#for döngüsü içine 2 tane eleman da atanabilir
for (i,j) in liste:
    print("i : {} j : {}".format(i,j))