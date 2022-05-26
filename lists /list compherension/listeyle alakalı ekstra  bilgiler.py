#append metodunu hatırlama
liste = [1,2,3,4]
liste.append(5)
#
liste1 = [1,2,3,4,5,6]
liste2= list()
for i in liste1:
    liste2.append(i)
print(liste2)
#list compherension
liste3 = [5,6,7,8,9,10]
liste4 = [i for i in liste3]
print(liste4 )

liste=[3,4,5]
liste1=[i*4 for i in liste]
print(liste1)
#string üzerinde gezinme
s ="Python"
liste=[i*3 for i in s]
print(liste)
#iç içe for döngüleri
liste=[[1,2,3],[4,5,6],[7,8,9]]
liste1=list()
for i in liste:
    for x in i:
        liste1.append(x)
print(liste1)