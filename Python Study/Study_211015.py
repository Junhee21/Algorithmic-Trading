#21 10 15
#PyQt5 익히기

#TUI VS GUI

import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) # pyqt5를 사용하기 위해선 QApplicaiton class의 객체를 생성해야 한다.

label = QLabel("Hello")
label.show()
# btn = QPushButton("Bye")
# btn.show()

app.exec_() # 이벤트 루프 생성
    # 이 코드가 없으면 파이썬은 코드를 다 실행하고 자동 종료된다.
    # 이벤트 루프는 우리가 끄기 전까지 gui 프로그램을 계속 실행하게 해준다. 일종의 반복문