# 21 10 07


# 21 06 29 ~ 21 10 06 backtesting
import pyupbit
import numpy as np

# OHLCV(open, highm low, close, volum) = 당일 시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count = 100) # 100일에 해당하는 ohlcv 얻기


# 변동폭*k = (고가-저가)*k
df['range'] = (df['high'] - df['low']) * 0.5 # k=0.5 로 설정

# target(매수가) : 위에서 구한 range를 shift(1)로 한칸씩 내려 매수가 결정
df['target'] = df['open'] + df['range'].shift(1)
 
# fee = 0.0032
# ror(수익률) : np.where(조건문, 참일때, 거짓일때)
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'], #- fee
                     1)

# 누적 수익률 계산
df['hpr'] = df['ror'].cumprod()

# Draw Down 계산
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# MDD 계산
print("MDD(%): ", df['dd'].max())

# 액셀로 출력
df.to_excel("last_100days_bitcoin.xlsx")