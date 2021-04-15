import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("hello2.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.pb_clicked)
    def pb_clicked(self):
        a = int(self.le1.text())
        b = int(self.le2.text())
        if a > b:
            print("작습니다.")
            return
        sum = 0
        for a in range(b+1):
            sum += a
        print(sum) 
        self.le3.setText(str(sum))

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()