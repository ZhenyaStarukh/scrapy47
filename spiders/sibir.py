import scrapy
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import ArticleThumbnail

class SibrealSpider(scrapy.Spider):
    name = 'sibreal'
    allowed_domains = ['https://www.sibreal.org/']
    start_url = 'https://www.sibreal.org/s?k=%D1%81%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8&tab=all&pi='
    other_params = '&r=any&pp=10'

    def start_requests(self):
        for page in range(1, 55):
            print(self.start_url + str(page) + self.other_params)
            request = Request(self.start_url + str(page) + self.other_params, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = ArticleThumbnail()
        content = response.xpath("//div[@id = 'content']//div[@class='row']/ul")
        for article_link in content.xpath('.//div/div/a'):
            item['discussion_url'] = article_link.xpath('.//@href').extract_first()
            print(item['discussion_url'])
            yield (item)