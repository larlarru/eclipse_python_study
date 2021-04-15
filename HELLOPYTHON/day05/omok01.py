import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

form_class = uic.loadUiType("omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
    
#       전역이 아니기 때문에 전역 만들려면 self.변수 이렇게 해줘야한다.  
#         button = QPushButton("", self)
#         button.setGeometry(1, 1, 40, 40)
#         button.setIcon(QIcon('0.png'))
#         button.setIconSize(QSize(40,40))
#         button.clicked.connect(self.pb_click)
        for i in range(10):
            i = i+1
            for j in range(10):
                j = j+1
                print("i : ",i)
                print("j : ",j)
                button = QPushButton("", self)
#                 if(i==1 and j == 1):
#                     button.setGeometry(i, j, 40, 40)
#                 elif(i>1 and j > 1):
#                     button.setGeometry(i*40, j*40, 40, 40)
                button.setGeometry(i*40, j*40, 40, 40)
                button.setIcon(QIcon('0.png'))
                button.setIconSize(QSize(40,40))
                button.clicked.connect(self.pb_click)
        
    def pb_click(self):
        print("a")
#         self.button.setIcon(QtGui.QIcon('C:\\workspace_python\\HELLOPYTHON\\day05\\1.png'))
    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()