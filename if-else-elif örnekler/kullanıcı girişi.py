print("""
***************************

Kullanıcı girişşi programı


***************************

""")
kullanıci_adı="Tolga"
paraloa="12345"

while True:

    kullanıcı = input("Kullanıcı adınızı giriniz : ")

    parola = input("Parolanızı giriniz:")
    if(kullanıcı==kullanıci_adı and parola != paraloa):
        print("parolanız yanlış")
    elif(kullanıcı!=kullanıci_adı and parola==paraloa):

        print("kullanıcı adınız yanlış")



    elif(kullanıcı==kullanıci_adı and parola==paraloa):
        print("Giriş Yaptınız...")

        break

    else:
        print("Hem kullanıcı adınız hem parolanız yanlıştır tekrar dene")