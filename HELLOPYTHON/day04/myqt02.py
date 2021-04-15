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
        self.pb.clicked.connect(self.pb_clicked)
#         self.pb.changeText.clicked.connect(self.changeText)
#         self.pb.clicked.connect(self.changeText)
    def pb_clicked(self):
        a = int(self.le.text())+1
        self.le.setText(str(a))
#         print("pb clicked")
#         print(self.lineEdit.text())
#         print(int(self.lineEdit.text())+1)
#         str_old = self.lineEdit.text()
#         print("str_old", str_old)
#         num_old = int(str_old)
#         print("num_old", num_old+1)
#         res = str(num_old)
#         self.lineEdit.setText(res)
#     def changeText(self):
#         print(int(self.lineEdit.text())+1)
#         self.lineEdit.setText(int(self.lineEdit.text())+1)

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()