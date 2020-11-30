import sys
from PyQt5 import QtWidgets,QtGui
import sqlite3


class Member():
    def __init__(self, ad, parola):
        self.ad = ad
        self.parola = parola


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.con = sqlite3.connect("database.db")

        self.cursor = self.con.cursor()

        self.cursor.execute("Create Table If not Exists members (kullanici_adi TEXT,parola TEXT)")
        self.con.commit()

    def init_ui(self):
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

    def oku(self):

        isim = self.kullanici_adi.text()
        par = self.parola.text()
        member = Member(isim, par)

        sender = self.sender()

        if sender.text() == "KAYDET":
            self.save(member)
        else:
            self.login(member)

    def login(self, member):

        sorgu = "Select * from members where kullanici_adi =? and parola= ?"
        self.cursor.execute(sorgu, (member.ad, member.parola))
        liste = self.cursor.fetchall()

        if len(liste) == 0:
            self.yazi_alani.setText("Yanlış giriş yaptınız!\nLütfen tekrar deneyiniz.")
        else:
            self.yazi_alani.setText("Başarılı şekilde giriş yaptınız.\n" + "Hoşgeldiniz " + member.ad)
            self.pen = Base()



    def save(self, member):

        sorgu = "Select * from members where kullanici_adi =? "
        self.cursor.execute(sorgu, (member.ad,))
        liste = self.cursor.fetchall()

        if len(liste) == 0:
            self.cursor.execute("Insert into members Values(?,?)", (member.ad, member.parola))
            self.con.commit()

            self.yazi_alani.setText("Kayıt başarılı şekilde oluşturulmuştur.")
        else:
            self.yazi_alani.setText("Bu isim ile kayıtlı kullanıcı bulunmaktadır.")






