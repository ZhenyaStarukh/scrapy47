import scrapy
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import ArticleThumbnail

class PravoRuSpider(scrapy.Spider):
    name = 'pravoru'
    allowed_domains = ['https://pravo.ru/']
    start_url = 'https://pravo.ru/search/?query=%D1%81%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8&page='

    def start_requests(self):
        for page in range(1, 10):
            print(self.start_url + str(page))
            request = Request(self.start_url + str(page), cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = ArticleThumbnail()
        content = response.xpath("//div[@class='tile grad_over']")
        for article_link in content.xpath('./a'):
            item['discussion_url'] = article_link.xpath('./@href').extract_first()
            print(item['discussion_url'])
            yield (item)