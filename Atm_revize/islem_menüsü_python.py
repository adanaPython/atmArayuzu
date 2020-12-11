from PyQt5 import QtWidgets,QtGui
from pencere1_paracek import Pencere1
from pencere2_parayatir import Pencere2
from pencere3_bakiyesor import Pencere3

class Base(QtWidgets.QWidget):

    def __init__(self,name):
        super().__init__()
        self.name = name
        self.init_ui()
        self.pencere1 = Pencere1(self.name)
        self.pencere2 = Pencere2(self.name)
        self.pencere3 = Pencere3(self.name)
        self.pencere1.signal.connect(self.pencere1Kapat)
        self.pencere2.signal1.connect(self.pencere2Kapat)
        self.pencere3.signal2.connect(self.pencere3Kapat)


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
        self.pencere1.show()

    def paraYatir(self):
        self.pencere2.show()

    def bakiyeSor(self):
        self.pencere3.show()

    def cikis(self):
        QtWidgets.qApp.quit()

    def pencere1Kapat(self):
        self.pencere1.close()

    def pencere2Kapat(self):
        self.pencere2.close()

    def pencere3Kapat(self):
        self.pencere3.close()



