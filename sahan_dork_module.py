from googlesearch import search
import os
def Ara(KelimeD,Dosya,Sayi,dil):
    for url in search(KelimeD,tld='com',start=0,lang=dil, stop=Sayi, pause=15.0):
        print(url)
        dosya = open(Dosya, 'a+')
        dosya.write(url +"\n")
        dosya.close()
#******************************************
def DorklarSql(Ara,kelime):
    print("İngilizce/English: en")
    print("Türkçe/Turkish: tr")
    print("Çince/China: zh")
    print("Rusça/Russia: ru")
    print("Arapça/Arabic: ar")
    print("Please Enter Country / Language to Choose:")
    dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
    print("Choose file name:('Examples: test.txt')")
    dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
    sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100):  "))
    Ara(kelime,dosya_adi,sayi,dil)
    print("**********************************************")
    print("***İLK TARAMA TAMAM İKİNCİ "+str(sayi)+" BAŞLATILIYOR*** ")
    print("****************BİLGİLERİ GİRİNİZ******************************")
    devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız")
    if devam == "y":
        print("İngilizce/English: en")
        print("Türkçe/Turkish: tr")
        print("Çince/China: zh")
        print("Rusça/Russia: ru")
        print("Arapça/Arabic: ar")
        print("Please Enter Country / Language to Choose:")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        kelime = "productlist.php?tid="
        Ara(kelime,dosya_adi,sayi,dil)
        print("***İKİNCİ TARAMA TAMAM ÜÇÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ="showsub.php?id="
        Ara(kelime,dosya_adi,sayi,dil)
        print("***ÜÇÜNCÜ TARAMA TAMAM DÖRDÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ="view_items.php?id="
        Ara(kelime,dosya_adi,sayi,dil)
        print("***DÖRDÜNCÜ TARAMA TAMAM SON "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ="_news/news.php?id="
        Ara(kelime,dosya_adi,sayi,dil)
        print("**********************************************")
        print("SQL DORKLARI BİTTİ YENİ DORKLARA GEÇİN VEYA MANUEL GİRİN")
        print("SQL DORKS FİNİSHED....")
        print("**********************************************")
        print("Continue is press y stop is press n")
        devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız:  ")
#**************************************
def DorklarXss(Ara,kelime):
    print("İngilizce: en")
    print("Türkçe: tr")
    print("Çince: zh")
    print("Rusça: ru")
    print("Arapça: ar")
    dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
    dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
    print("Choose file name:('Examples: test.txt')")
    sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100)(""):  "))
    Ara(kelime,dosya_adi,sayi,dil)
    print("**********************************************")
    print("***İLK TARAMA TAMAM İKİNCİ "+str(sayi)+" BAŞLATILIYOR*** ")
    print("****************BİLGİLERİ GİRİNİZ******************************")
    devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız: ")
    if devam == "y":
        print("İngilizce/English: en")
        print("Türkçe/Turkish: tr")
        print("Çince/China: zh")
        print("Rusça/Russia: ru")
        print("Arapça/Arabic: ar")
        print("Please Enter Country / Language to Choose:")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        kelime = 'inurl:".php?years="'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***İKİNCİ TARAMA TAMAM ÜÇÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='inurl:".php?txt="'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***ÜÇÜNCÜ TARAMA TAMAM DÖRDÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='inurl:com_feedpostold/feedpost.php?url='
        Ara(kelime,dosya_adi,sayi,dil)
        print("***DÖRDÜNCÜ TARAMA TAMAM SON "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='(inurl:headersearch.php?sid='
        Ara(kelime,dosya_adi,sayi,dil)
        print("**********************************************")
        print("SQL DORKLARI BİTTİ YENİ DORKLARA GEÇİN VEYA MANUEL GİRİN")
        print("SQL DORKS FİNİSHED....")
        print("**********************************************")
        print("Continue is press y stop is press n")
        devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız")
    if devam == "n":
        print("Sql Dorkları için 1: ")
        print("WordPress Dorkları için 2: ")
        print("Xss Dorkları için 3: ")
        print("File Dorkları için 4: ")
        print("Pass Dorkları için 5: ")
        print("Kamera Dorkları için 6: ")
        print("Manuel(elle) Dork Girmek için 7 basınız: ")
        print("KAPATMAK İÇİN q BASINIZ")
#*************************************
def DorklarWp(Ara,kelime):
    print("İngilizce/English: en")
    print("Türkçe/Turkish: tr")
    print("Çince/China: zh")
    print("Rusça/Russia: ru")
    print("Arapça/Arabic: ar")
    print("Please Enter Country / Language to Choose:")
    dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
    print("Choose file name:('Examples: test.txt')")
    dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
    sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100)(""):  "))
    Ara(kelime,dosya_adi,sayi,dil)
    print("**********************************************")
    print("***İLK TARAMA TAMAM İKİNCİ "+str(sayi)+" BAŞLATILIYOR*** ")
    print("****************BİLGİLERİ GİRİNİZ******************************")
    devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız: ")
    if devam == "y":
        print("İngilizce: en")
        print("Türkçe: tr")
        print("Çince: zh")
        print("Rusça: ru")
        print("Arapça: ar")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        kelime = '("uncategorized/hello-world")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***İKİNCİ TARAMA TAMAM ÜÇÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='("author/admin")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***ÜÇÜNCÜ TARAMA TAMAM DÖRDÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='("Proudly powered by WordPress")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***DÖRDÜNCÜ TARAMA TAMAM SON "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='("Welcome to WordPress. This is your first post.")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("**********************************************")
        print("SQL DORKLARI BİTTİ YENİ DORKLARA GEÇİN VEYA MANUEL GİRİN")
        print("SQL DORKS FİNİSHED....")
        print("**********************************************")
        print("Continue is press y stop is press n")
        devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız")
    if devam == "n":
        print("Sql Dorkları için 1: ")
        print("WordPress Dorkları için 2: ")
        print("Xss Dorkları için 3: ")
        print("File Dorkları için 4: ")
        print("Pass Dorkları için 5: ")
        print("Kamera Dorkları için 6: ")
        print("Manuel(elle) Dork Girmek için 7 basınız: ")
        print("KAPATMAK İÇİN q BASINIZ")
#*************************************
def DorklarPass(Ara,kelime):
    print("İngilizce/English: en")
    print("Türkçe/Turkish: tr")
    print("Çince/China: zh")
    print("Rusça/Russia: ru")
    print("Arapça/Arabic: ar")
    print("Please Enter Country / Language to Choose:")
    dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
    print("Choose file name:('Examples: test.txt')")
    dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
    sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100)(""):  "))
    Ara(kelime,dosya_adi,sayi,dil)
    print("**********************************************")
    print("***İLK TARAMA TAMAM İKİNCİ "+str(sayi)+" BAŞLATILIYOR*** ")
    print("****************BİLGİLERİ GİRİNİZ******************************")
    devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız: ")
    if devam == "y":
        print("İngilizce: en")
        print("Türkçe: tr")
        print("Çince: zh")
        print("Rusça: ru")
        print("Arapça: ar")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        kelime = '"whoops! there was an error." "db_password"'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***İKİNCİ TARAMA TAMAM ÜÇÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='("phpMyAdmin MySQL-Dump" filetype:txt")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***ÜÇÜNCÜ TARAMA TAMAM DÖRDÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='("your password is" filetype:log")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***DÖRDÜNCÜ TARAMA TAMAM SON "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='(allintitle: restricted filetype: mail")'
        Ara(kelime,dosya_adi,sayi,dil)
        print("**********************************************")
        print("SQL DORKLARI BİTTİ YENİ DORKLARA GEÇİN VEYA MANUEL GİRİN")
        print("SQL DORKS FİNİSHED....")
        print("**********************************************")
        print("Continue is press y stop is press n")
        devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız")
    if devam == "n":
        print("Sql Dorkları için 1: ")
        print("WordPress Dorkları için 2: ")
        print("Xss Dorkları için 3: ")
        print("File Dorkları için 4: ")
        print("Pass Dorkları için 5: ")
        print("Kamera Dorkları için 6: ")
        print("Manuel(elle) Dork Girmek için 7 basınız: ")
        print("KAPATMAK İÇİN q BASINIZ")
#*************************************
def DorklarCamera(Ara,kelime):
    print("İngilizce/English: en")
    print("Türkçe/Turkish: tr")
    print("Çince/China: zh")
    print("Rusça/Russia: ru")
    print("Arapça/Arabic: ar")
    print("Please Enter Country / Language to Choose:")
    dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
    print("Choose file name:('Examples: test.txt')")
    dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
    sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100)(""):  "))
    Ara(kelime,dosya_adi,sayi,dil)
    print("**********************************************")
    print("***İLK TARAMA TAMAM İKİNCİ "+str(sayi)+" BAŞLATILIYOR*** ")
    print("****************BİLGİLERİ GİRİNİZ******************************")
    devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız: ")
    if devam == "y":
        print("İngilizce: en")
        print("Türkçe: tr")
        print("Çince: zh")
        print("Rusça: ru")
        print("Arapça: ar")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        kelime = '“Powered by WebcamXP” “Pro|Broadcast”'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***İKİNCİ TARAMA TAMAM ÜÇÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='intitle:”My WebcamXP Server!” inurl:”8080″'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***ÜÇÜNCÜ TARAMA TAMAM DÖRDÜNCÜ "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='inurl:”webcam7″ intitle:”8080″'
        Ara(kelime,dosya_adi,sayi,dil)
        print("***DÖRDÜNCÜ TARAMA TAMAM SON "+str(sayi)+" BAŞLATILIYOR*** ")
        kelime ='intitle:”Live View / – AXIS” | inurl:view/views.html'
        Ara(kelime,dosya_adi,sayi,dil)
        print("**********************************************")
        print("SQL DORKLARI BİTTİ YENİ DORKLARA GEÇİN VEYA MANUEL GİRİN")
        print("SQL DORKS FİNİSHED....")
        print("**********************************************")
        print("Continue is press y stop is press n")
        devam = input ("Devam Edilsin Diyorsanız y dursun diyorsanız n basınız")
    if devam == "n":
        print("Sql Dorkları için 1: ")
        print("WordPress Dorkları için 2: ")
        print("Xss Dorkları için 3: ")
        print("File Dorkları için 4: ")
        print("Pass Dorkları için 5: ")
        print("Kamera Dorkları için 6: ")
        print("Manuel(elle) Dork Girmek için 7 basınız: ")
        print("KAPATMAK İÇİN q BASINIZ")
#*************************************
