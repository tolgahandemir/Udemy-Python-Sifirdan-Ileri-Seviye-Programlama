liste=[]
liste1=[]

for a in range(1,101):
    liste.append(a)
    for a in liste1:
        liste1.append(a)
    if(a%2==0):
        print(a)
