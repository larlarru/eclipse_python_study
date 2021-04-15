import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("hello3.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
    def pb_clicked(self):
        a = self.le1.text()
        b = round(random.random() * 10)
        if(b%2 ==0):
            b = "짝"
        elif(b%2 != 0):
            b = "홀"
        
        if(a==b):
            res ="이겼습니다."
        else:
            lbl_red = QLabel('Red')
            lbl_red.setStyleSheet("color: red;")
            vbox = QVBoxLayout()
            vbox.addWidget(lbl_red)
            res = "졌습니다."
            self.le3.setText(res)
            self.le3.setLayout(vbox)
        
        self.le2.setText(b)
        
#         self.le3.setText(res)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()