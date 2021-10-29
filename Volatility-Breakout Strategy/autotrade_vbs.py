# 21/10/29
# 변동성 돌파 전략을 사용한 자동매매 코드 구현



import time
import pyupbit
import datetime


# class 정의
class Info:
    def __init__(self, ticker, k):
        self.df = self.get_df_ohlcv(ticker)
        self.now = datetime.datetime.now()
        self.start_time = self.get_start_time(ticker)
        self.end_time = self.start_time+datetime.timedelta(days=1)
        self.balance = self.get_balance(ticker)
        self.krw = self.get_balance("KRW")
        self.current_price = self.get_current_price(ticker)
        self.target_price = self.get_target_price(k)

    def get_df_ohlcv(self, ticker, interval='day', count=1): # ohlcv dataframe 형으로 변환
        return pyupbit.get_ohlcv(ticker, interval = 'day', count = 1)

    def get_start_time(self, ticker): # 기준 시간 설정 (KST 09:00)
        start_time = self.df.index[0]
        return start_time
    
    def get_balance(self, ticker): # 잔고 조회
        return upbit.get_balance(ticker)

    def get_current_price(self, ticker): # 현재가 조회
        return pyupbit.get_orderbook(tickers=ticker)[0]["orderbook_units"][0]["ask_price"]

    def get_target_price(self, k): # 변동성 돌파 전략을 통한 매수 목표가 반환
        target_price = self.df.iloc[0]['close'] + (self.df.iloc[0]['high'] - self.df.iloc[0]['low']) * k
        return target_price



# 업비트 API, 변수 선언
access = "access key"
secret = "secret key"

ticker = "KRW-BTC"
k = 0.3
interval = 10

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
while True:
    try:
        vbs = Info(ticker, k)
        if vbs.start_time < vbs.now < vbs.end_time - datetime.timedelta(seconds=11): # 매수(09:00~08:59:50)
            if vbs.target_price < vbs.current_price:
                if vbs.krw > 5000:
                    upbit.buy_market_order(ticker, vbs.krw*0.9995)
        else:
            if vbs.balance > 0.00008:
                upbit.sell_market_order(ticker, vbs.balance*0.9995)
    except:
        print("ERROR")
    time.sleep(interval)