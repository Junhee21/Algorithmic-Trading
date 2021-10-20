#21 10 16
#PyQt5 익히기

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic


class Mywindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 100, 400, 800)
        self.setWindowTitle("Hihi")
        self.setWindowIcon(QIcon('flood_house_water_natural_phenomenon_catastrophe_icon_194190.png'))

        btn1 = QPushButton("button 1", self)
        btn1.move(10,10)
        btn1.clicked.connect(self.btn_clicked) #이벤트처리
        btn2 = QPushButton("button 2", self)
        btn2.move(10,40)

    def btn_clicked(self): #콜백 함수
        print("Click!")


form_class = uic.loadUiType("window211016_1.ui")[0]
class Mywindow2(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        

app=QApplication(sys.argv) #QApplication 객체 생성

window=Mywindow2()
window.show()

app.exec_() # 객체 생성부터 여기까지 이벤트루프 생성