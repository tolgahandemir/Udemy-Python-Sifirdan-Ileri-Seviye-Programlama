while True:
    isim=input("İsminizi Giriniz:")
    soy_isim=input("Soyadınızı giriniz :")
    if(isim =="q"):
        print("Program sonlandırıldı")
        break
    print("İsminiz : {}\nSoyadınız : {}".format(isim,soy_isim))