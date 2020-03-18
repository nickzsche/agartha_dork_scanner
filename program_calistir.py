from googlesearch import search
import os
from sahan_dork_module import *

while True:
    print("Program Başlatılıyor: ")
    print("************************************************")
    print("**********AGARTHA SOFTWARE ŞAHAN HASRET*********")
    print("************************************************")
    print("Start Program")
    
    print("Sql Dorks 1: ")
    print("WordPress Dorks 2: ")
    print("Xss Dorks 3: ")
    print("Camera Dorks 4: ")
    print("Pass Dorks 5: ")
    print("Manuel(elle) Dork Girmek için 0 basınız: ")
    print("Manuel Dorks to write press 0: ")
    print("Kapatmak için q basınız")
    print("Press q to quit")
    dorksecici= input("")
    if dorksecici =="1":
        kelime="view_items.php?id="
        DorklarSql(Ara,kelime)
    if dorksecici=="2":
        kelime='("Comment on Hello world!")'
        DorklarWp(Ara,kelime)
    if dorksecici=="3":
        kelime='inurl:".php?cmd="'
        DorklarXss(Ara,kelime)
    if dorksecici=="4":
        DorklarCamera(Ara,kelime)
        kelime ='intitle:”Android Webcam Server” inurl:”8080″'
    if dorksecici=="5":
        DorklarPass(Ara,kelime)
        kelime = 'inurl:admin/password.txt'
    if dorksecici =="0":
        dorkObek= input("Aranacak Dorku Yazınız: (Dosya içindeki bin klasörü altındaki dorklar dosyasında var): ")
        dosya_adi = input("Lütfen Dosya Yolu veya Adı Seçin(Sonuna Mutlaka .txt Koyun):  ")
        sayi= int(input("Kaç Adet Arama Yapılsın?(Max:100):  "))
        print("İngilizce/English: en")
        print("Türkçe/Turkish: tr")
        print("Çince/China: zh")
        print("Rusça/Russia: ru")
        print("Arapça/Arabic: ar")
        print("Please Enter Country / Language to Choose:")
        dil = input("Lütfen Seçilecek Ülke/Dil Uzantısını Giriniz: ")
        Ara(dorkObek,dosya_adi,sayi,dil)
    if dorksecici =="q":
        exit()
            
