# news_crawling
BBC most read top10 news HTML crawling + NewsAPI recent news real-time crawling

## 📌 프로젝트 개요
이 프로젝트는 뉴스 데이터를 수집하고, MongoDB 또는 Cassandra에 저장하는 시스템입니다. BBC Most Read 기사를 Selenium을 활용해 크롤링하거나, NewsAPI를 통해 최신 뉴스를 받아서 데이터베이스에 저장합니다.

## 📂 파일 구조 및 주요 함수
'''
.
├── main.py               # 프로그램 실행 스크립트 (데이터 크롤링 및 DB 저장 실행)
│   ├── argparse 설정 및 실행 인자 처리
│   ├── crawl_bbc_most_read() 실행 (BBC Most Read 크롤링)
│   ├── fetch_newsapi_articles() 실행 (NewsAPI 크롤링)
│   ├── MongoDB 또는 Cassandra에 데이터 저장
│   └── DB 연결 종료
├── MongoDB.py            # MongoDB 관련 함수 (데이터 저장, 연결 종료 등)
│   ├── save_article(article_url, content) - BBC 크롤링 데이터 저장
│   ├── save_newsapi_article(article) - NewsAPI 데이터 저장
│   └── close_connection() - MongoDB 연결 종료
├── Cassandra.py          # Cassandra 관련 함수 (데이터 저장, 연결 종료 등)
│   ├── connect_to_cassandra() - Cassandra 연결 설정
│   ├── save_article(article_url, content) - BBC 크롤링 데이터 저장
│   ├── save_newsapi_article(article) - NewsAPI 데이터 저장
│   └── close_connection() - Cassandra 연결 종료 (현재 별도 종료 없음)
├── NewsAPI.py            # NewsAPI에서 뉴스 데이터를 가져오는 스크립트
│   ├── fetch_newsapi_articles(db_choice) - NewsAPI 데이터를 가져와 DB에 저장
├── selenium_crawler.py   # Selenium을 이용한 BBC Most Read 기사 크롤링
│   ├── crawl_bbc_most_read() - BBC Most Read 섹션 크롤링 (기사 URL, 본문 추출)
└── README.md             # 프로젝트 설명 문서
'''
## ✅ 주의 사항
MongoDB 및 Cassandra의 데이터베이스 및 테이블/컬렉션이 미리 설정되어 있어야 합니다.

Selenium 크롤러 사용 시 크롬 드라이버가 필요합니다 (webdriver-manager를 사용하여 자동 설치됨).

## 🚀 실행 방법
### 1. 환경 설정

Python 3.x 필요

필요한 라이브러리 설치:

'''
pip install cassandra-driver pymongo requests selenium webdriver-manager
'''

MongoDB와 Cassandra가 실행 중이어야 합니다.

NewsAPI 사용을 위해 API 키가 필요합니다.

### 2. 실행 명령어 예시

MongoDB에 저장하고, BBC & NewsAPI 둘 다 크롤링하려면:

'''
python main.py --db mongodb --source both
'''

Cassandra에 저장하고, NewsAPI 데이터만 가져오려면:

'''
python main.py --db cassandra --source newsapi
'''



