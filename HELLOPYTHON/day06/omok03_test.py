import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

form_class = uic.loadUiType("omok03.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        
        self.icon0 = QIcon('0.png')
        self.icon1 = QIcon('1.png')
        self.icon2 = QIcon('2.png')
        
        self.arr2dpb = []
        
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0],
                [0,0,0,0,0, 0,0,0,0,0]
            ]
        
    
        for i in range(10):
            line = []
            for j in range(10):
                button = QPushButton("", self)
                button.setGeometry(j*40, i*40, 40, 40)
                button.setToolTip(str(i)+","+str(j))
                button.setIconSize(QSize(40,40))
                button.setIcon(self.icon0)
                line.append(button)
                button.clicked.connect(self.pb_click)
            self.arr2dpb.append(line)
        self.myrender()
        
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.arr2dpb[i][j].setIcon(self.icon0)
                elif self.arr2d[i][j] == 1:
                    self.arr2dpb[i][j].setIcon(self.icon1)
                elif self.arr2d[i][j] == 2:
                    self.arr2dpb[i][j].setIcon(self.icon2)
                
    def pb_click(self):
        print(self.sender().toolTip())
        a = self.sender().toolTip()
        a = a.split(",")
        print("aa : ",a[0])
        print("bb : ",a[1])
        i = int(a[0])
        j = int(a[1])
        self.arr2d[i][j] = 1
        print(self.arr2d[i][j])
        
        rndi = round(random.random())
        rndj = round(random.random())
        print(rndi)
        print(rndj)
        if(self.arr2d[rndi][rndj] == 0):
            self.arr2d[rndi][rndj] = 2
        else:
            return
            
        self.myrender()


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()