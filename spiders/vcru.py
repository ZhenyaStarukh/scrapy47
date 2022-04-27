import scrapy
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import ArticleThumbnail

class VcSpider(scrapy.Spider):
    name = 'vcru'
    allowed_domains = ['https://vc.ru/']
    start_url = "https://vc.ru/search/v2/content/relevant?query=%D0%A1%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8%20"

    def start_requests(self):
        print(self.start_url)
        request = Request(self.start_url, cookies={'store_language': 'en'}, callback=self.parse)
        yield request

    def parse(self, response):
        item = ArticleThumbnail()
        content = response.xpath("//div[@class = 'l-page__content']")
        for article_link in content.xpath(".//a[@class='content-link']"):
            item['discussion_url'] = article_link.xpath('./@href').extract_first()
            print(item['discussion_url'])
            yield (item)