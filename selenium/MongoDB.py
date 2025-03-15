from pymongo import MongoClient

# MongoDB 연결
client = MongoClient("mongodb://localhost:27017/")  # 로컬 MongoDB 실행 중이어야 함
db = client["newsapi_db"] # 데이터베이스 newsapi_db 생성
collection = db["most_read"] # 컬렉션: MongoDB에서 문서(document)들의 모음. RDBMS에서 테이블과 유사. 없으면 자동으로 생성됨.

def save_article(article_url, content):
    """크롤링한 뉴스 기사를 DB에 저장하는 함수"""
    article_data = {
        "url": article_url,
        "content": content
    }
    collection.insert_one(article_data)
    print(f"데이터 저장 완료: {article_url}")

def save_newsapi_article(article):
    """
    NewsAPI에서 가져온 기사 데이터를 MongoDB에 저장
    """
    article_data = {
        "url": article["url"],
        "source_id": article["source"]["id"] if article["source"]["id"] else "unknown",
        "source_name": article["source"]["name"] if article["source"]["name"] else "unknown",
        "author": article["author"] if article["author"] else "unknown",
        "title": article["title"],
        "description": article["description"] if article["description"] else "No description available",
        "urlToImage": article["urlToImage"] if article["urlToImage"] else "No image",
        "publishedAt": article["publishedAt"],
        "content": article["content"] if article["content"] else "No content available"
    }
    collection.insert_one(article_data)
    print(f"MongoDB 저장 완료: {article['title']}")


# DB 연결 종료 함수
def close_connection():
    client.close()
