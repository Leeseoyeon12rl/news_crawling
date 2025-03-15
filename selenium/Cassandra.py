from cassandra.cluster import Cluster

def connect_to_cassandra():
    """Cassandra 데이터베이스 연결"""
    cluster = Cluster(["127.0.0.1"])  # Docker에서 실행 시 기본 IP
    session = cluster.connect()
    session.set_keyspace("newsapi_data")  # 기존에 powershell에서 docker를 통해 만든 Keyspace 사용. 미리 만들어둬야 함.
    return session

def save_article(article_url, content):
    """크롤링한 기사 데이터를 Cassandra에 저장"""
    session = connect_to_cassandra()
    
    session.execute(
        """
        INSERT INTO most_read (url, content)
        VALUES (%s, %s)
        """,
        (article_url, content)
    )
    print(f"Cassandra 데이터 저장 완료: {article_url}")


def save_newsapi_article(article):
    """
    NewsAPI에서 가져온 기사 데이터를 Cassandra에 저장
    """
    session = connect_to_cassandra()

    session.execute("""
        INSERT INTO news_articles (url, source_id, source_name, author, title, description, urlToImage, publishedAt, content)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        article["url"],
        article["source"]["id"] if article["source"]["id"] else "unknown",
        article["source"]["name"] if article["source"]["name"] else "unknown",
        article["author"] if article["author"] else "unknown",
        article["title"],
        article["description"] if article["description"] else "No description available",
        article["urlToImage"] if article["urlToImage"] else "No image",
        article["publishedAt"],
        article["content"] if article["content"] else "No content available"
    ))

    print(f"Cassandra 저장 완료: {article['title']}")

def close_connection():
    """Cassandra 연결 종료 (현재는 클러스터를 닫지 않음)"""
    print("Cassandra 연결 종료 (연결 풀 방식이므로 별도 종료 없음)")
