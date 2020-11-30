import sys
from PyQt5 import QtWidgets,QtGui
import sqlite3


class Member():     #veritabanına eklenecek banka hesaplarını oluşturmaya yarayacak ad ve paroladan oluşan class
    def __init__(self, ad, parola):
        self.ad = ad
        self.parola = parola


class Pencere(QtWidgets.QWidget):   #Database adında bir veritabanı oluşturan giriş yapmaya yada banka hesabı kaydı oluşturmaya yarayan class. 

    def __init__(self):

        super().__init__()

        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self): #database adında bir veritabanı oluşturuldu.
        self.con = sqlite3.connect("database.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("Create Table If not Exists members (kullanici_adi TEXT,parola TEXT)") #members adında bir tablo oluşturduk.kullanici_adi ve parola sütunlarına sahip.
        self.con.commit()

    def init_ui(self): #ilk giriş ekranımızın tasarımı.
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)  # parolanın görünmez olmasını sağlıyor.
        self.yazi_alani = QtWidgets.QLabel("")
        self.giris = QtWidgets.QPushButton("GİRİŞ")
        self.kayit = QtWidgets.QPushButton("KULLANICI KAYDET")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.giris)
        v_box.addWidget(self.kayit)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")

        self.giris.clicked.connect(self.oku)
        self.kayit.clicked.connect(self.oku)
        self.show()

    def oku(self):  #kullanici ve parola yazi alanlarina yazilmiş olan verileri okuyoruz.

        isim = self.kullanici_adi.text()
        par = self.parola.text()
        member = Member(isim, par) #member sınıfından bir obje ürettik.

        sender = self.sender()

        if sender.text() == "KAYDET": #kaydet ya da giriş butonuna basılmış olmasına göre farklı fonksiyonlara dallandırıyoruz.
            self.save(member)
        else:
            self.login(member)
            
    def save(self, member): #kullaniciyi kaydetmek istiyorsak buraya dallanacak.

        sorgu = "Select * from members where kullanici_adi =? " #aynı kullaniciyi birden çok oluşturmamak için database'de kayıt var mı?
        self.cursor.execute(sorgu, (member.ad,))
        liste = self.cursor.fetchall()

        if len(liste) == 0: #liste boş gelmişse kayıt yok. Veritabanına kayıt et.
            self.cursor.execute("Insert into members Values(?,?)", (member.ad, member.parola))
            self.con.commit()

            self.yazi_alani.setText("Kayıt başarılı şekilde oluşturulmuştur.")
        else: #liste boş gelmemişse.
            self.yazi_alani.setText("Bu isim ile kayıtlı kullanıcı bulunmaktadır.")

    def login(self, member): #girişe basılmış ise dallanan fonksiyon

        sorgu = "Select * from members where kullanici_adi =? and parola= ?"
        self.cursor.execute(sorgu, (member.ad, member.parola)) #kullanıcı adı ve parola database'de kayıtlı mı?
        liste = self.cursor.fetchall()

        if len(liste) == 0: #eğer kayıtlı dağil ise liste boş dönmüştür ve giriş yapılmayacaktır.
            self.yazi_alani.setText("Yanlış giriş yaptınız!\nLütfen tekrar deneyiniz.")
        else: #eğer kayıtlı ise liste boş dönmemiştir ve giriş yapılacaktır.
            self.yazi_alani.setText("Başarılı şekilde giriş yaptınız.\n" + "Hoşgeldiniz " + member.ad)
            
            self.pen = Base() #base isimli bir class'a yönlendirecek.



    






