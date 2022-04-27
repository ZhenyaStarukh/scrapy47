import scrapy
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import ArticleThumbnail

class PnpSpider(scrapy.Spider):
    name = 'pnpru'
    allowed_domains = ['https://www.pnp.ru/']
    start_url = 'https://www.pnp.ru/search/articles/'
    other_params = '/?query=%D0%A1%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8'

    def start_requests(self):
        for page in range(1, 10):
            print(self.start_url + str(page) + self.other_params)
            request = Request(self.start_url + str(page) + self.other_params, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = ArticleThumbnail()
        content = response.xpath("//div[@class='mat_listing search_listing']")
        for article_link in content.xpath('./div/a'):
            item['discussion_url'] = article_link.xpath('./@href').extract_first()
            print(item['discussion_url'])
            yield (item)