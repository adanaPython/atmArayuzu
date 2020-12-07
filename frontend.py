import sys
from PyQt5 import QtWidgets,QtGui
import sqlite3

class Member():
    def __init__(self,ad,parola,balance):
        self.ad = ad
        self.parola = parola
        self.balance = balance

class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("Create Table If not Exists members (kullanici_adi TEXT,parola TEXT , bakiye INT)")
        self.con.commit()

    def init_ui(self):
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.parola = QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) #parolanın görünmez olmasını sağlıyor.
        self.yazi_alani = QtWidgets.QLabel("")
        self.giris = QtWidgets.QPushButton("GİRİŞ")
        self.kayit = QtWidgets.QPushButton("KAYDET")

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

    def oku(self):
        isim = self.kullanici_adi.text()
        par = self.parola.text()
        sender = self.sender()

        if sender.text() == "KAYDET" :
            sorgu = "Select * from members where kullanici_adi =? and parola= ?"
            self.cursor.execute(sorgu, (isim, par))
            liste = self.cursor.fetchall()
            if len(liste) == 0:
                bak = 0
                member = Member(isim, par, bak)
                self.yazi_alani.setText("Kayıt oluşturulmuştur.")
                self.save(member)
            else:
                self.yazi_alani.setText("Sistemde kaydetmek istediğiniz isimde kullanıcı bulunmaktadır.")

        else:
            self.login(isim,par)

    def login(self,isim,par):
        sorgu = "Select * from members where kullanici_adi =? and parola= ?"
        self.cursor.execute(sorgu, (isim, par))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            self.yazi_alani.setText("Yanlış giriş yaptınız!\nLütfen tekrar deneyiniz.")
        else:
            self.yazi_alani.setText("Başarılı şekilde giriş yaptınız.\n" + "Hoşgeldiniz " + liste[0][0])
            self.ui = Base(liste[0][0])

    def save(self,member):
        sorgu = "Select * from members where kullanici_adi =? "
        self.cursor.execute(sorgu, (member.ad,))
        liste = self.cursor.fetchall()
        if len(liste) == 0:
            self.cursor.execute("Insert into members Values(?,?,?)", (member.ad, member.parola,member.balance))
            self.con.commit()
            self.yazi_alani.setText("Kayıt başarılı şekilde oluşturulmuştur.")
        else:
            self.yazi_alani.setText("Bu isim ile kayıtlı kullanıcı bulunmaktadır.")

class Base(QtWidgets.QWidget):
    def __init__(self,name):
        super().__init__()
        self.name = name
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("ANA MENÜ")
        self.setGeometry(100, 100, 500, 500)
        self.yaziAlani = QtWidgets.QLabel("PYTHON Bank'a Hoşgeldiniz")
        self.buton = QtWidgets.QPushButton("Para Çek")
        self.buton1 = QtWidgets.QPushButton("Para Yatır")
        self.buton2 = QtWidgets.QPushButton("Bakiye Sor")
        self.buton3 = QtWidgets.QPushButton("Çıkış")
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("python.jpeg"))

        v_box = QtWidgets.QVBoxLayout()
        h_box =QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.logo)
        h_box.addStretch()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.yaziAlani)
        h_box1.addStretch()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box2.addWidget(self.buton)
        h_box2.addWidget(self.buton1)
        h_box3 = QtWidgets.QHBoxLayout()
        h_box3.addWidget(self.buton2)
        h_box3.addWidget(self.buton3)
        v_box.addStretch()
        v_box.addLayout(h_box)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addLayout(h_box3)
        v_box.addStretch()

        self.setLayout(v_box)

        self.buton.clicked.connect(self.paraCek)
        self.buton1.clicked.connect(self.paraYatir)
        self.buton2.clicked.connect(self.bakiyeSor)
        self.buton3.clicked.connect(self.cikis)

        self.show()

    def paraCek(self):
        self.pencere1 = Pencere1(self.name)

    def paraYatir(self):
        self.pencere2 = Pencere2(self.name)

    def bakiyeSor(self):
        self.pencere3 = Pencere3(self.name)

    def cikis(self):
        QtWidgets.qApp.quit()

class Pencere1(QtWidgets.QWidget):
    def __init__(self,name):
            super().__init__()
            self.name = name
            self.init_ui()
    def init_ui(self):
        self.setWindowTitle("PARA ÇEKME")
        self.setGeometry(100, 100, 500, 500)
        self.yaziAlani = QtWidgets.QLineEdit("")
        self.etiket = QtWidgets.QLabel("Çekmek istediğiniz miktarı yaz")
        self.etiket2 = QtWidgets.QLabel("")
        self.buton =QtWidgets.QPushButton("TAMAM")
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("python.jpeg"))

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.logo)
        h_box1.addStretch()
        v_box.addLayout(h_box1)
        h_box2.addWidget(self.etiket2)
        v_box.addLayout(h_box2)
        v_box.addStretch()
        h_box.addWidget(self.etiket)
        h_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        self.setLayout(v_box)

        self.buton.clicked.connect(self.call1)

        self.show()

    def call1(self):
        self.miktar = int(self.yaziAlani.text())

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        sorgu = "Select * from members where kullanici_adi =?"
        self.cursor.execute(sorgu, (self.name,))
        liste = self.cursor.fetchall()

        if ( liste[0][2] >= self.miktar ) :
            yeni_bakiye = liste[0][2] - self.miktar
            sorgu2 = "Update members set bakiye =? where kullanici_adi=? "
            self.cursor.execute(sorgu2, (yeni_bakiye, self.name))
            self.con.commit()
            self.etiket2.setText("Sayın " + self.name + " yeni bakiyeniz " + str(yeni_bakiye) + " TL'dir")
        else:
            self.etiket2.setText("Yetersiz bakiye..")

class Pencere2(QtWidgets.QWidget):
    def __init__(self,name):
            super().__init__()
            self.name = name
            self.init_ui()
    def init_ui(self):
        self.setWindowTitle("PARA YATIR")
        self.setGeometry(100, 100, 500, 500)
        self.yaziAlani = QtWidgets.QLineEdit("")
        self.etiket = QtWidgets.QLabel("Yatırmak istediğiniz miktarı yaz")
        self.etiket1 = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("TAMAM")
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("python.jpeg"))

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box1.addStretch()
        h_box1.addWidget(self.logo)
        h_box1.addStretch()
        v_box.addLayout(h_box1)
        h_box2.addStretch()
        h_box2.addWidget(self.etiket1)
        h_box2.addStretch()
        v_box.addLayout(h_box2)
        v_box.addStretch()
        h_box.addWidget(self.etiket)
        h_box.addWidget(self.yaziAlani)
        v_box.addLayout(h_box)
        v_box.addWidget(self.buton)
        v_box.addStretch()
        self.setLayout(v_box)

        self.buton.clicked.connect(self.call2)

        self.show()

    def call2(self):
        self.miktar = int(self.yaziAlani.text())

        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
        sorgu = "Select * from members where kullanici_adi =?"
        self.cursor.execute(sorgu,(self.name,))
        liste = self.cursor.fetchall()

        if len(liste) == 0:
            print("Aradığınız isimde bir kullanıcı kayıtlı değildir..")
        else:
            yeni_bakiye = self.miktar + liste[0][2]
            sorgu2 = "Update members set bakiye =? where kullanici_adi=? "
            self.cursor.execute(sorgu2, (yeni_bakiye, self.name))
            self.con.commit()

        self.etiket1.setText("Sayın " +self.name + " yeni bakiyeniz " + str(yeni_bakiye) + " TL'dir"  )

class Pencere3(QtWidgets.QWidget):
    def __init__(self,name):
            super().__init__()
            self.name = name
            self.init_ui()
    def init_ui(self):
        self.setWindowTitle("BAKİYE ÖĞRENME")
        self.setGeometry(100, 100, 500, 500)

        self.con = sqlite3.connect("database.db")

        self.cursor = self.con.cursor()
        sorgu = "Select * from members where kullanici_adi =?"
        self.cursor.execute(sorgu, (self.name,))
        liste = self.cursor.fetchall()

        self.etiket = QtWidgets.QLabel("Sayın " + self.name + " Bakiyeniz  " + str(liste[0][2]) +" TL")

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.etiket)
        h_box.addStretch()
        self.setLayout(h_box)
        self.show()

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()

sys.exit(app.exec_())
