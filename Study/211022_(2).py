# 21/10/22
# 웹 API
# RestfulAPI : 웹 주소를 사용해서 상호작용을 하는 웹 API

# RestfulApi 예시
# https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw

# ? 왼쪽 오른쪽으로 구분해서 생각 / 왼쪽을 함수처럼 오른쪽을 파라미터 처럼

import requests

r = requests.get("https://api.korbit.co.kr/v1/ticker/detailed?currency_pair=btc_krw")
print(r.text)
print(type(r.text)) # 문자열 객체

# requests.get으로 얻은 데이터는 JSON(JavaScript Object Notation) 포맷이다
# 파이썬에서 해당 데이터를 쉽게 다루기 이해 JSON 포맷을 dictionary type 으로 변경하자
bitcoin_dic = r.json()
print(bitcoin_dic)
print(type(bitcoin_dic)) # dic으로 변경 되었음을 확인 = dictionary 메소드 사용 가능

print(bitcoin_dic['volume'])

import datetime
timestamp = bitcoin_dic['timestamp']
timestamp_date = datetime.datetime.fromtimestamp(timestamp/1000)
print(timestamp_date)