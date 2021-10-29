# 21/10/29
# 변동성돌파 전략 백테스팅(backtesting)
# 최근 1년간



from pandas._libs.tslibs.timestamps import Timestamp
import pyupbit
import numpy as np


# class 정의
class backtesting:
    def __init__(self, ticker, k, terms, fee):

        # ohlcv 데이터를 dataframe으로 반환
        self.df = pyupbit.get_ohlcv(ticker, count= terms, period= 1)

        # 변동폭(range = high - low)을 column에 추가
        self.df['range'] = (self.df['high'] - self.df['low'])

        # 목표가(=매수가, target) = 당일 시가(=전날 종가) + (전날 range * k)
        self.df['target'] = self.df['open'] + (self.df['range'].shift(1))*k

        # 고가가 목표가보다 높다면 매수
        # 수익률(rate of return)=매도가(종가에 자동 판매)/매수가(목표가)*매수수수료(100%-fee)*매도수수료(100%-fee)
        self.df['ror'] = np.where(self.df['high'] > self.df['target'],
                            self.df['close'] / self.df['target'] * (1-fee/100) * (1-fee/100), 1)

        # 누적수익률(= 보유기간수익률, holding period return)
        self.df['hpr'] = self.df['ror'].cumprod()

        # 낙폭(Draw Down)
        # cumax = cumulative max 
        self.df['dd'] = (self.df['hpr'].cummax() - self.df['hpr']) / self.df['hpr'].cummax() * 100

        # 최대낙푝(Max Draw Down)
        self.mdd = self.df['dd'].max()

        # 최종수익률
        # 마지막 날은 아직 끝나지 않았으므로 그 전날 누적수익률
        self.final_ror = self.df['hpr'][-2]



# 출력
# k = 0 부터 1 까지 0.1 씩
for k in np.arange(0, 1.1, 0.1):
    # 전달인자 = ticker, k(parameter), backtesting기간(days), 업비트 수수료 0.05%
    bt = backtesting("KRW-BTC", k, 365, 0.05)

    # 자동매매 안하고 보유한 경우
    if k == 0:  # 먼저 한번만 출력
        no_vbs = bt.df['close'][-2]/bt.df['open'][0]
        print("if no vbs, only holing ror : ", no_vbs)
    
    print("if k = %.1f, ror = %.5f, mdd = %.5f" %(k, bt.final_ror, bt.mdd))


# 액셀로 출력
# df.to_excel("VBS_backtesting.xlsx")