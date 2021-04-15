import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import random

form_class = uic.loadUiType("hello7.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb1.clicked.connect(self.pb_clicked)
        self.pb2.clicked.connect(self.pb_clicked)
        self.pb3.clicked.connect(self.pb_clicked)
    def pb_clicked(self):
        mine = self.sender().text()
        
        rnd = random.random()
        com = ""
        if(rnd >= 0.6):
            com ="가위"
        elif(rnd < 0.6):
            com ="바위"
        elif(rnd <= 0.3):
            com ="보"
        
        if mine == com:
            result = "비겼습니다."
        elif mine == "가위":
            if com == "바위":
                result = "졌습니다."
            elif com == "보":
                result = "이겼습니다."
        elif mine == "바위":
            if com == "보":
                result = "졌습니다."
            elif com == "가위":
                result = "이겼습니다."
        elif mine == "보":
            if com == "가위":
                result = "졌습니다."
            elif com == "바위":
                result = "이겼습니다."
            
        
        self.le1.setText(mine)
        self.le2.setText(com)
        self.le3.setText(result)
        
        
        
        
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()