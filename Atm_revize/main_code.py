
from PyQt5.QtWidgets import QApplication
from kullanici_giris_python import Pencere

class KullaniciGiris():

    def __init__(self):
        super().__init__()
        self.pencere = Pencere()
        self.pencere.show()




app = QApplication([])

pencere_kullanici = KullaniciGiris()

app.exec_()