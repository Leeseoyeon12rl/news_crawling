'''
실행 전 세팅:
MongoDB.py -> 데이터베이스 선택, 컬렉션 목록 확인
Cassandra.py -> 데이터베이스 선택, 테이블 목록 확인
crawler.py -> 크롤링할 기사 개수 변경
NewsAPI.py -> params 변경 및 실시간 크롤링 여부 선택

실행 명령어 예시:
python main.py --db mongodb --source both | python main.py --db cassandra --source newsapi
'''

import argparse
import MongoDB
import Cassandra
import NewsAPI
from selenium_crawler import crawl_bbc_most_read

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="Chosse a database to store articles")
    parser.add_argument("--db", choices=["mongodb", "cassandra"], required=True, help="Database selection: mongodb or cassandra")
    parser.add_argument("--source", choices=["bbc", "newsapi", "both"], default="both", help="Data source selection")

    args = parser.parse_args()

    # BBC Most Read 크롤링 실행
    if args.source in ["bbc", "both"]:
        articles = crawl_bbc_most_read()
        if articles:
            for article_url, content in articles:
                if args.db == "mongodb":
                    MongoDB.save_article(article_url, content)
                elif args.db == "cassandra":
                    Cassandra.save_article(article_url, content)

    
    # NewsAPI 크롤링 실행
    if args.source in ["newsapi", "both"]:
        NewsAPI.fetch_newsapi_articles(args.db)
        
    # 연결 종료
    if args.db == "mongodb":
        MongoDB.close_connection()
    elif args.db == "cassandra":
        Cassandra.close_connection()