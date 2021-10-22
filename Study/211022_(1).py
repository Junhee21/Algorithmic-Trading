# 21/10/22
# 웹 스크래핑

import requests
from bs4 import BeautifulSoup

#접속할 도메인 문자열로 지정
url = "https://finance.naver.com/item/main.naver?code=005930"

#get함수의 반환값인 Response 객체 바인딩
#Response는 클래스이므로 메소드 이용가능
samsung_elec_stock = requests.get(url).text

# HTML 코드 txt로 저장
fw=open('삼성전자주가_html.txt', 'w', encoding='utf-8')
fw.write(samsung_elec_stock)
fw.close()

# HTML에서 데이터 파싱
# 파싱(parsing) : 어떤 페이지에서 내가 원하는 데이터를 특정 패턴으로 추출해 가공하는 것
#만든 객체로 메소드 사용 가능
soup = BeautifulSoup(samsung_elec_stock, "html5lib")

# CSS id컬렉터 : id가 _per인 태그를 select
per_taglist = soup.select("#_per")

#select는 조건에 만족하는 모든 태그를 리스트로 변환 ->리스트 메소드 사용가능
first_per = per_taglist[0]
print("now Saumsung_elect per : ", first_per.text)



#위에서 만든 것을 class로 구현
class Naver_Stock:
    def __init__(self, code):
        self.code = code
        self.url = "https://finance.naver.com/item/main.naver?code=" + code
        self.html = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html, "html5lib")
    def get_per(self):
        self.tags = self.soup.select("#_per")
        self.tag = self.tags[0]
        return float(self.tag.text)
    def get_dividend(self):
        self.tags = self.soup.select("#_dvr")
        self.tag = self.tags[0]
        return float(self.tag.text)
    # 크롬 웹페이지에서 원하는 부분 우클릭 후 검사
    # 해당 태그 우클릭 > copy > copy selector 로 selector 자동으로 얻기
    def get_B_A(self):
        self.tags = self.soup.select("#tab_con1 > div:nth-child(3) > table > tbody > tr.strong > td > em")
        self.tag = self.tags[0]
        return self.tag.text

samsung_elec_code = Naver_Stock("005930")
sk_hynix_code = Naver_Stock("000660")
kakao_code = Naver_Stock("035720")

print("Saumsung_elect - per ", samsung_elec_code.get_per())
print("SkHynix - per ", sk_hynix_code.get_per())
print("Kakao - per ", kakao_code.get_per())
print("Saumsung_elect - dividend ", samsung_elec_code.get_dividend())
print("SkHynix - dividend ", sk_hynix_code.get_dividend())
print("Kakao - dividend ", kakao_code.get_dividend())
print("Saumsung_elect - B_A ", samsung_elec_code.get_B_A())
print("SkHynix - B_A ", sk_hynix_code.get_B_A())
print("Kakao - B_A ", kakao_code.get_B_A())