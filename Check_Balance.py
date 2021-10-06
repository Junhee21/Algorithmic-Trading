# 21 10 07
import pyupbit

#로그인
access = "본인 값으로 변경"
secret = "본인 값으로 변경"
upbit = pyupbit.Upbit(access, secret)

#잔고조회
print("CASH : ", upbit.get_balance("KRW"))         # 보유 현금 조회
print("BTC : ",upbit.get_balance("KRW-BTC"))       # 보유 코인 조회
print("ETH : ",upbit.get_balance("KRW-ETH"))
print("ETC : ",upbit.get_balance("KRW-ETC"))
print("XRP : ",upbit.get_balance("KRW-XRP"))
print("DOGE : ",upbit.get_balance("KRW-DOGE"))