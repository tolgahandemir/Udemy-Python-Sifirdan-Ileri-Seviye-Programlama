total = 0
while True :
    number =input("Sayıyı giriniz : ")


    if(number=="q"):
        break
    number=int(number)
    total +=number

print(total)
