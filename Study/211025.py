# 21/10/25

# 판다스(pandas) 모듈은 1차원, 2차원 데이터를 쉽게 다룰 수 있게 하는 타입을 제공한다.
from pandas import Series # Series 1차원 데이터 구조

d1_data_1 = [100, 200, 300, 400]
series_1 = Series(d1_data_1)

print(series_1)
print(type(series_1))

# index value 지정 int뿐만 아니라 str도 가능
data_arr = ['2021-10-23','2021-10-24','2021-10-25','2021-10-26']
d1_data_2 = [3, 4, 2, 1]
series_2 = Series(d1_data_2, index=data_arr)
print(series_2)

# 리스트와 마찬가지로 indexing, slicing 가능
# series_2['2021-10-23'] = series_2[0]
# 기존의 iterator slicing과 차이점 : 끝 값이 포함된다
print("series slicing\n",series_2['2021-10-24':'2021-10-26']) # 마지막 값 포함됨
print("series slicing by int iterator\n",series_2[0:2]) # 마지막 값 포함X


series_2['2121-10-27'] = 100 # insert
print("result of insergin\n",series_2)
print(series_2.drop('2021-10-23')) # delete(drop)

# 리스트 안에 데이터는 for문으로 연산해되지만 Series는 한번에 된다
print(series_2*10)



from pandas import DataFrame # 2차원 데이터 자료구조

d2_data = {'open':[100,200,300], 'high':[110,210,300]} # dictionary 이용해 만듬
df1 = DataFrame(d2_data)
print(df1)

d2_data_coffee = {'Americano':[2000,2500,3000,5000],
                    'Latte':[3000,3000,4000,5000], 'Caramel':[4000,4500,5000,6000]}
df_coffee = DataFrame(d2_data_coffee, index=['A', 'B', 'C', 'D'])
print("Table of Coffee\n",df_coffee)



# 외부 데이터(excel, web_page) 가져오기

# excel data 처리하기 
import pandas as pd
df2 = pd.read_excel("C:\Junhee\Algorithmic Trading\last_100days_bitcoin.xlsx")
# df2.set_index('date') #index로 지정하고 싶은 column 이름 넘기기
print(df2)
# excel 로 저장하소 싶을 때는 pd.to_excel("파일명.xlsx")


# Web page data 처리하기
import requests
kakao_chart_url = "https://finance.naver.com/item/sise_day.nhn?code=035270"
df_kakao = pd.read_html(requests.get(kakao_chart_url, headers={'User-agent': 'Mozilla/5.0'}).text)
print(df_kakao[0].dropna(axis=0))

s = Series([100, 200, 300]) 
s2 = s.shift(1)
s3 = s.shift(-1)
print(s) 
print(s2)
print(s3)