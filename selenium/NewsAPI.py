# API 요청을 보내 JSON 데이터 수집.
# NewsAPI 서버에서 JSON 형태로 뉴스 목록 제공받음.
# 구조화된 데이터/API 사용량 일일 제한 있음/일부 유료.
# 실시간 크롤링 원한다면: while True 루프, time.sleep()를 추가하여 일정 시간마다 크롤링하다록 변경하기
    # def fetch_newsapi_articles(db_choice, interval=600):, while True:와 time.sleep() 사이 코드 모두 tab하여 실행행

# 일반 크롤러(Selenium, BeautifulSoup)와 다르게 할 필요 없는 것.
'''
✅ 브라우저 실행 필요 없음 (Selenium처럼 웹브라우저를 띄울 필요 없음)
✅ HTML 파싱 필요 없음 (BeautifulSoup으로 find() 할 필요 없음)
✅ JavaScript 로딩 기다릴 필요 없음 (Playwright/Selenium의 wait 필요 없음)
👉 API를 요청하면 바로 데이터가 JSON으로 오기 때문에 빠르고 안정적임!
'''

import requests
import MongoDB
import Cassandra

# NewsAPI 설정
API_KEY = "b995ef3649f34239aa4e072c4e9155f9"
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_newsapi_articles(db_choice):
    """
    NewsAPI에서 최신 뉴스를 가져와서 MongoDB|Cassandra에 저장
    - db_choice: "mongodb" or "cassandra"
    """
#while True:
    params = {
        "country": "us", # 미국 뉴스
        "category": "technology", # 기술 뉴스
        #"pageSize": 20 # 최대 20개 가져오기
        "apiKey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        for article in articles:
            url = article["url"]
            content = article["content"] if article["content"] else "내용 없음"

            if db_choice == "mongodb":
                MongoDB.save_newsapi_article(article)
            elif db_choice == "cassandra":
                Cassandra.save_newsapi_article(article)
            else:
                print("지원되지 않는 DB 선택!")

    else:
        print(f"NewsAPI 오류 발생: {response.status_code}, {response.text}")
    
    #time.sleep(interval)