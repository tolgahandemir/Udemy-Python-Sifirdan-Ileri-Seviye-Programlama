print("""
******************************

Mükemmel Sayı Bulma Programı

Exit to Program for 'q'
******************************

""")
number = int(input("Sayıyı Giriniz : "))
i= 1
toplam = 0
while True :
    while(i<number):
        if(number % i ==0):
            toplam += i
        i += 1
    if(toplam==number):
        print("mükemmel sayıdır")
        break
    else:
        print("mükemmel sayı değildir")
        break