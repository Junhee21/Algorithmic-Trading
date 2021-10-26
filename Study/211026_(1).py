# 21/10/26

import pybithumb
import time
import datetime

tickers = pybithumb.get_tickers()
print("tickers num in Bithumb : ", len(tickers))

# for i in range(1,3):
#     price = pybithumb.get_current_price("BTC")
#     print(price)
#     time.sleep(1)

print("BTC Price : ", pybithumb.get_current_price("BTC"))
ohlv = pybithumb.get_market_detail("BTC")
print("BTC Open High Low Volume : ", ohlv)
for i in range(0,10):
    try:
        print(ohlv[i])
    except:
        print("out of bounds")

orderbook = pybithumb.get_orderbook("BTC")
ms = int(orderbook["timestamp"])
dt = datetime.datetime.fromtimestamp(ms/1000)
print("Now time : ", dt)

bids = orderbook["bids"]
asks = orderbook["asks"]

print("-------bids-------")
for b in bids:
    print(b)
print("-------asks-------")
for a in asks:
    print(a)

print("\n\n")
all = pybithumb.get_current_price("ALL")
for k, v in all.items():
    print("ticker : ", k)
    print(v)
