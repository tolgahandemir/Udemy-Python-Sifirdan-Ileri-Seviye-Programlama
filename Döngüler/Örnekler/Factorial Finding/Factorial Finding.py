print("""
****************************

Factorial Finding
Exit to program for 'q'
****************************

""")
process_id= "q"
while True :
    process=input("Sayıyı Giriniz : ")
    if(process == process_id):
        print("Exit to Program")
        break
    else :
        process=int(process)
        factoriel = 1

        for i in range(2,process+1):
            factoriel *= i
        print("Factoriel : ",factoriel)