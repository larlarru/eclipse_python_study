import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtGui, QtCore

form_class = uic.loadUiType("omok01.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.initUI()
#         self.pb.clicked.connect(self.pb_clicked)

    def initUI(self):
        pb2 = QPushButton(self)
        pb2.setIcon(QtGui.QIcon('C:\\workspace_python\\HELLOPYTHON\\day05\\0.png'))
        pb2.setGeometry(40, 40, 40, 40)
        pb2.setIconSize(QtCore.QSize(40,40))
#         self.lbl1.clicked.connect(self.lbl_clicked)
#     def pb_clicked(self):
# #         img = QtGui.QPixmap('C:\\workspace_python\\HELLOPYTHON\\day05\\1.png')
# #         self.lbl1.setPixmap(img)
#         self.pb.setIcon(QtGui.QIcon('C:\\workspace_python\\HELLOPYTHON\\day05\\1.png'))
#     def lbl_clicked(self):
#         print("a")
    


if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()