# 웹사이트의 HTML을 직접 분석하는 일반 웹 크롤러 selenium 사용.
# 특정 태그(XPath)에서 뉴스 url, 본문 추출.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def crawl_bbc_most_read():
    """BBC 뉴스 Most Read 섹션에서 상위 10개 기사 크롤링"""
    print("크롤러 시작됨")
    
    # Chrome 브라우저 실행 옵션 설정
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 브라우저 창 없이 실행
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36")

    # WebDriver 실행
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # BBC Most Read 페이지 열기
    url = "https://www.bbc.com/news"
    driver.get(url)
    time.sleep(random.uniform(3, 6))  # 페이지 로딩 대기 (랜덤 딜레이)

    print("📌 현재 URL:", driver.current_url)
    print("📌 현재 페이지 제목:", driver.title)
    
    # Most Read 기사 링크 찾기
    try:
        # 페이지가 완전히 로드될 때까지 대기
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='main-content']/article/section[6]/div/div[2]/div/div/a/div/div/div/h2")))
        
        articles = driver.find_elements(By.XPATH, "//*[@id='main-content']/article/section[6]/div/div[2]/div/div/a")
        article_links = []

        for article in articles:
            link = article.get_attribute("href")
            if link and "https://www.bbc.com/news" in link:
                article_links.append(link)

        article_links = list(set(article_links))[:10]  # 중복 제거 후 상위 10개 선택
        print(f"✅ Most Read 기사 {len(article_links)}개 링크 수집 완료")

    except Exception as e:
        print(f"❌ XPath 에러: {e}")
        driver.quit()
        return None
    
    # 여러 개의 기사 데이터를 저장할 리스트 생성
    articles_data =[]

    # 기사 본문 크롤링
    for article_url in article_links:
        driver.get(article_url)
        time.sleep(random.uniform(3, 6))  # 랜덤 딜레이 추가

        try:
            paragraphs = driver.find_elements(By.XPATH, "//article//p")
            content = "\n".join([p.text for p in paragraphs if p.text.strip()])

            print(f"✅ 크롤링 성공: {article_url}")
            print(f"✅ 크롤링된 본문: {content[:100]}...")

            # 크롤링한 기사 데이터를 리스트에 저장
            articles_data.append((article_url, content))
            
        except Exception as e:
            print(f"❌ 본문 크롤링 실패: {e}")

    driver.quit()
    
    return articles_data # 여러 개의 기사 데이터를 반환