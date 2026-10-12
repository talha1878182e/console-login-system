import time

print ("Site Giriş Sayfasına Hoş Geldiniz")

user1 = "TalhaCebecioglu"
password1 ="1234"

while True:
    kullanici = input("Kullanıcı Adı: ")
    sifre = input("Sifre: ")
    if kullanici == user1 and sifre == password1:
        print ("Bilgiler Kontrol Ediliyor...")
        time.sleep(1.5)
        print("Giriş Başarılı")
        break
    elif (kullanici != user1) and (sifre == password1):
        print ("Kullanıcı Adı Hatalı Tekrar Deneyiniz")
    elif (kullanici == user1) and (sifre != password1):
        print ("Şifre Hatalı")
        print("Tekrar Denemek İster misiniz?(Evet/Hayır)")
        cevap= input()
        if cevap == "Hayır":
            print("Şifrenizi Değiştirmek ister misiniz?(Evet/Hayır)")
            cevap= input()
            if cevap == "Evet":
                newpassword1= input("Yeni Sifrenizi Girin: ")
                print("Şifre Değiştiriliyor Lütfen Bekleyin...")
                time.sleep(1.5)
                print("Şifre Başarılıyla Değiştirildi")
                password1=newpassword1
    else:
        print("Sanırım Bilgilerinizi Yalnış Girdiniz Tekrar Deneyiniz")
