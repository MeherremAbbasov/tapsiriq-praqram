sinif = []


ad=input("Adinizi Yaz: ")
soyad=input("Soyadinizi yaz: ")
nomre=input("Nomrenizi Yazin: ")
email=input("Emailnizi Yazin: ")


class telebe:
    def __init__(self,_ad,_soyad,_nomre,_email):
        self.ad=_ad
        self.soyad=_soyad
        self.nomre=_nomre
        self.email=_email

        def baza(self):
         print(f"Sizin Adiniz:{self.ad},Soyadiniz:{self.soyad},Nomreniz:{self.nomre},Emailiniz:{self.email}")


ad=input("Adinizi Yaz:")
soyad=input("Soyadinizi yaz:")
nomre=input("Nomrenizi Yazin:")
email=input("Emailnizi Yazin:")

telebeobiyekt=telebe(ad,soyad,nomre,email)

sinif=append(telebeobiyekt)


ad2=input("Adinizi Yaz:")
soyad2=input("Soyadinizi yaz:")
nomre2=input("Nomrenizi Yazin:")
email2=input("Emailnizi Yazin:")

telebeobiyekt2=telebe(ad,soyad,nomre,email)

sinif=append(telebeobiyekt2)



print(sinif)





