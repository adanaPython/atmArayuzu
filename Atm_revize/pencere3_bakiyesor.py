from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtCore import pyqtSignal


class Pencere3(QtWidgets.QWidget):

    signal2 = pyqtSignal()

    def __init__(self, name):
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

        self.etiket = QtWidgets.QLabel("Sayın " + self.name + " Bakiyeniz  " + str(liste[0][2]) + " TL")
        self.buton_cikis = QtWidgets.QPushButton("BİR ÖNCEKİ MENÜ")


        v_box = QtWidgets.QVBoxLayout()


        v_box.addWidget(self.etiket)
        v_box.addStretch()
        v_box.addWidget(self.buton_cikis)
        v_box.addStretch()
        self.setLayout(v_box)

        self.buton_cikis.clicked.connect(self.call1)

    def call1(self):
        self.signal2.emit()
