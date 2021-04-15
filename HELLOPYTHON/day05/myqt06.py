import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random
from PyQt5.QtWidgets import QMessageBox


form_class = uic.loadUiType("hello4.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.pbnum_clicked)
        self.pb2.clicked.connect(self.pbnum_clicked)
        self.pb3.clicked.connect(self.pbnum_clicked)
        self.pb4.clicked.connect(self.pbnum_clicked)
        self.pb5.clicked.connect(self.pbnum_clicked)
        self.pb6.clicked.connect(self.pbnum_clicked)
        self.pb7.clicked.connect(self.pbnum_clicked)
        self.pb8.clicked.connect(self.pbnum_clicked)
        self.pb9.clicked.connect(self.pbnum_clicked)
        self.pb0.clicked.connect(self.pbnum_clicked)
        
        self.pb.clicked.connect(self.pb_clicked)
    def pbnum_clicked(self):
        sender = self.sender().text()
        res = self.le1.text()
        self.le1.setText(res + sender)
    def pb_clicked(self):
        QMessageBox.about(self, "Calling", self.le1.text())

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()