# 21/10/26
# bull market or bear market

import pybithumb
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic


# 해당 ticker의 ohlcv가 dataframe 객체"btc"에 저장
btc = pybithumb.get_ohlcv("BTC")

open_price = btc['open']
close_price = btc['close']


# 이동평균선(moving average) = 설정기간의 종가의 합/설정기간
# 주가의 평균치 진행방향을 확인하고 대략적인 상승과 하락 동향을 예측
# window = close_price.rolling(5)  5일씩 모든 데이터를 그룹화
# ma5 = window.mean()  평균계산
# 위에 코드 합쳐서
ma5 = close_price.rolling(5).mean()

def bull_market(ticker):
    ohlcv = pybithumb.get_ohlcv(ticker)
    ma7 = ohlcv['close'].rolling(window=7).mean()
    price = pybithumb.get_current_price(ticker)
    last_ma7 = ma7[-2]
    if (price > last_ma7):
        print(ticker, "OOO Bull market")
    else:
        print(ticker, "XXX Bear market")

tickers = pybithumb.get_tickers()
# for ticker in tickers:
#     bull_market(ticker)
#     time.sleep(0.1)


# Make Gui Bull or Bear
from_class = uic.loadUiType("C:/Junhee/QtDesigner/bull_or_bear.ui")[0]
tickers = ["BTC", "ETH", "BCH", "ETC"]

class Mywindow(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def get_market_infos(self, ticker):
        df = pybithumb.get_ohlcv(ticker)
        ma7 = df['close'].rolling(window=7).mean()
        last_ma7 = ma7[-2]
        price = pybithumb.get_current_price(ticker)
        state = None
        if price > last_ma7:
            state = "Bull"
        else:
            state = "Bear"
        return price, last_ma7, state
    
    def timeout(self):
        for i, ticker in enumerate(tickers):
            item = QTableWidgetItem(ticker)
            self.tableWidget.setItem(i, 0, item)

            price, last_ma7, state = self.get_market_infos(ticker)
            self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma7)))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(state)))

app = QApplication(sys.argv)
win = Mywindow()
win.show()
app.exec_()