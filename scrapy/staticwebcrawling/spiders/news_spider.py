'''실행: scrapy crawl news -o news.json'''

import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    start_urls = ["https://www.bbc.com/korean/articles/cd65w8y9qd9o/"]

    def parse(self, response):
        for article in response.css("div.article"):
            yield {
                "title": article.css("h2::text").get(),
                "link": article.css("a::attr(href)").get(),
                "published_date": article.css("span.date::text").get(),
            }

# Scrapy가 가져온 HTML에 본문이 포함되지 않았다.
# = BBC가 본문을 JavaScript를 통해 동적으로 로드하고 있다는 의미.

# Scrapy만으로 본문을 가져올 수 없으며, Selenium 같은 도구를 사용하여 Javascript 렌더링을 수행해야 한다.

# 또한 Selenium은 Scrapy와 다르게 독립적으로 실행되는 브라우저 자동화 도구이므로,
# Scrapy 프로젝트 폴더(staticwebcrawling)와는 무관하게 어디서든 실행할 수 있다. -> 일반적인 Python 스크립트처럼 실행하면 됨.
# Scrapy의 경우, powershell에서 'scrapy startproject staticwebcrawling' 명령어를 통해 scrapy 프로젝트를 생성했음.