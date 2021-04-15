import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("hello.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #버튼에 기능을 연결하는 코드
#         self.pb.clicked.connect(self.pb_click)
#      #btn_1이 눌리면 작동할 함수
#      def pb_click(self):
#          print("click")
#          self.lbl.setText("Good Evening")

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()