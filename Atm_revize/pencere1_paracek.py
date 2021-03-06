from PyQt5 import QtWidgets,QtGui
import sqlite3
from PyQt5.QtCore import pyqtSignal


class Pencere1(QtWidgets.QWidget):

    signal = pyqtSignal()

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
        self.butoncikis = QtWidgets.QPushButton("BİR ÖNCEKİ MENÜ")
        self.logo = QtWidgets.QLabel()
        self.logo.setPixmap(QtGui.QPixmap("python.jpeg"))

        v_box = QtWidgets.QVBoxLayout()
        h_box = QtWidgets.QHBoxLayout()
        h_box1 = QtWidgets.QHBoxLayout()
        h_box2 = QtWidgets.QHBoxLayout()
        h_box3 = QtWidgets.QHBoxLayout()
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
        h_box3.addWidget(self.butoncikis)
        v_box.addLayout(h_box3)
        v_box.addStretch()
        self.setLayout(v_box)

        self.buton.clicked.connect(self.call1)
        self.butoncikis.clicked.connect(self.call2)



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

    def call2(self):
        self.signal.emit()

