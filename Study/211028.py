# 21/10/27

# 스레드(thread)

import sys
import pybithumb
import time
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("C:/Junhee/QtDesigner/bull_or_bear.ui")[0]

class Worker(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        while True:
            data = {}
            for ticker in tickers:
                data[ticker] = self.get_market_infos(ticker)
            self.finished.emit(data)
            self.sleep(2)
    
    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(5).mean()
            last_ma5 = ma5[-2]
            price = pybithumb.get_current_price(ticker)
            state = None
            if price>last_ma5:
                state = "UPUP Bull"
            else:
                state = "DOWN Bear"
            return price, last_ma5, state
        except:
            return None, None, None


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tableWidget.setItem(index, 0, QTableWidgetItem(ticker))
                self.tableWidget.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tableWidget.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tableWidget.setItem(index, 3, QTableWidgetItem(str(infos[2])))
        except:
            pass

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()