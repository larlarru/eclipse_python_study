from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(180, 234)
 
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(20, 160, 141, 61))
        self.listWidget.setObjectName("textBrowser")
 
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 10, 16, 16))
        self.label.setObjectName("label")
 
 
        self.startButton = QtWidgets.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(50, 130, 75, 23))
        self.startButton.setObjectName("startButton")
 
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(30, 30, 113, 20))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
 
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #startButton 클릭시 autoExcute 함수 수행
        self.startButton.clicked.connect(self.autoExcute)
 
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Naver Login"))
        self.label.setText(_translate("Dialog", "ID"))
        self.startButton.setText(_translate("Dialog", "시작"))
 
 #셀레니움 동작 코드 함수 autoExcute 생성
    def autoExcute(self):
        driver  = webdriver.Chrome('C:\workspace_python\HELLOPYTHON\day09\chromedriver.exe')
        driver.implicitly_wait(3)
        driver.get('http://www.naver.com')
        driver.maximize_window()
        id = self.lineEdit_ID.text()
        driver.find_element_by_class_name('lg_local_btn').click()
        driver.find_element_by_id('id').send_keys(id)
        driver.find_element_by_class_name('btn_global').click()
        time.sleep(3)
        driver.close()
        #listWidget에 로그인 성공 표시
        self.listWidget.addItem('로그인 성공')
        # self.addItem()
 
 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


