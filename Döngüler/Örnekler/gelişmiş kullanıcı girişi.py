print("""
**********************************
Kullanıcı Girişi Programı
**********************************
""")
sys_kullanıcı="Tolga"
sys_parola="1238"
giriş_hakkı=3
while True:
    kullanıcı=input("Kullanıcı adınızı giriniz: ")
    parola=input("Parolanızı giriniz :")
    if(kullanıcı!=sys_kullanıcı and parola==sys_parola):
        print("Kullanıcı adınız yanlış....")
        giriş_hakkı -=1
    elif(kullanıcı==sys_kullanıcı and parola!=sys_parola):
        print("Parolanız yanlış.....")
        giriş_hakkı -=1
    elif(kullanıcı!=sys_kullanıcı and parola!=sys_parola):
        print("Kullanıcı adınız ve Parolanız yanlış.....")
        giriş_hakkı-=1
    else:
        print("Sisteme başarıyla giriş yapılmıştır")
        break
    if(giriş_hakkı==0):
        print("Giriş hakkınız bitmiştir")
        break
