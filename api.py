from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
from datetime import datetime
from requests.api import get

# 무슨 프로그램인지 출력
print("이 프로그램은 허위정보와 과대광고가 있는 식품을 알려주는 프로그램입니다! ")

# 서비스 키가 들어있는 secret.json 파일오픈
with open("secret.json") as f:
    secret = json.loads(f.read())
    
# api 호출
url = 'http://apis.data.go.kr/1470000/FoodFlshdErtsInfoService/getFoodFlshdErtsList'

# 전송할 데이터들을 딕셔너리로 표현 (& 뒤의 값들을 의미)
queryParams = '?' + urlencode(
    {
        # 한글이 깨지지 않도록 quote_plus 사용
        # 인증키
        quote_plus('ServiceKey'): secret['SERVICE_KEY'],
        # 한 페이지의 결과 수 입력
        quote_plus('numOfRows'): 3,
        # 페이지 번호 입력
        quote_plus('pageNo'): 1,
        # json형식으로 출력되도록 함
        quote_plus('type'): 'json'
    }
)
# 한글로 받아온 데이터를 다시 풀어줌 
get_data = requests.get(url+unquote(queryParams))

# 코드가 올바른지 확인하기 위함 (200이 출력되어야 정상) 
# print(get_data.status_code)

# json으로 받은 res를 딕셔너리로 저장
res = get_data.json()

# 딕셔너리로 저장된 res를 출력
print(res)