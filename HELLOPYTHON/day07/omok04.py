import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

form_class = uic.loadUiType("omok04.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.flag_wb = True
        self.play = True
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
                button.setIconSize(QSize(40, 40))
                button.setIcon(self.icon0) 
                button.setToolTip(str(i)+","+str(j))
                button.clicked.connect(self.pb_click)
                line.append(button)
            self.arr2dpb.append(line)
        self.myrender()

    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0 :
                    self.arr2dpb[i][j].setIcon(self.icon0) 
                elif  self.arr2d[i][j] == 1 :    
                    self.arr2dpb[i][j].setIcon(self.icon1) 
                elif  self.arr2d[i][j] == 2 :    
                    self.arr2dpb[i][j].setIcon(self.icon2)   

    def pb_click(self) :
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] >0 :
            return
        
        stone_info = 0
        if self.flag_wb :
            self.arr2d[i][j]=1
            stone_info = 1
        else:
            self.arr2d[i][j]=2
            stone_info = 2
        
        up = self.getUP(i,j,stone_info)
        print("up",up)
        dw = self.getDW(i,j,stone_info)
        print("dw",dw)
        
        le = self.getLE(i,j,stone_info)
        print("le",le)
        ri = self.getRI(i,j,stone_info)
        print("ri",ri)
        
        ur = self.getUR(i,j,stone_info)
        print("ur",ur)
        ul = self.getUL(i,j,stone_info)
        print("ul",ul)
        
        dr = self.getDR(i,j,stone_info)
        print("dr",dr)
        dl = self.getDL(i,j,stone_info)
        print("dl",dl)
        
        self.myrender()
        self.flag_wb = not self.flag_wb
        
#         if up + dw == 4 or le + ri == 4 or ur + dl == 4 or ul + dr == 4:
#             print("이겼습니다.")
#             QMessageBox.about(self, "결과", "이겼습니다.")
        
        if up + dw >= 4 or le + ri >= 4 or ur + dl >= 4 or ul + dr >= 4:
            QMessageBox.about(self, "결과", "이겼습니다.")
            self.reset()
    
    def reset(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 1 :
                    self.arr2dpb[i][j].setIcon(self.icon0) 
                elif  self.arr2d[i][j] == 2 :    
                    self.arr2dpb[i][j].setIcon(self.icon0) 
        
    def getUP(self,i,j,stone_info):
        
        
        cnt = 0
        while True:
            i -= 1
            if i < 0:
                return cnt
            if j < 0:
                return cnt
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getDW(self,i,j,stone_info):
        cnt = 0
        while True:
            i += 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getLE(self,i,j,stone_info):
        cnt = 0
        while True:
            j += 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getRI(self,i,j,stone_info):
        cnt = 0
        while True:
            j -= 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getUR(self,i,j,stone_info):
        cnt = 0
        while True:
            i -=1
            j += 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getUL(self,i,j,stone_info):
        cnt = 0
        while True:
            i -=1
            j -= 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getDR(self,i,j,stone_info):
        cnt = 0
        while True:
            i +=1
            j += 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
    def getDL(self,i,j,stone_info):
        cnt = 0
        while True:
            i +=1
            j -= 1
            try:
                if self.arr2d[i][j] == stone_info:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
       
          
        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()
    
    
    
    
    
    
    
    