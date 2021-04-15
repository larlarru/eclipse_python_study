from selenium import webdriver
import time
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import sys

form_class = uic.loadUiType("selnium.ui")[0]

browser = webdriver.Chrome()
browser.get("http://localhost:8081/WEB2/mylogin")
browser.get("http://localhost:8081/WEB2/mycrawl")

menus = browser.find_element_by_tag_name('table')
ttt = menus.text
print(ttt)

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btn_clicked)
        
    def btn_clicked(self):
        self.te.setText(ttt)
#         print("pb_click")
#         arr_td = self.browser.find_elements_by_css_selector("td")
#         
#         print(arr_td)
#         
#         for i in arr_td:
#             print(i.text)
#             self.te.setText(i.text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
    
