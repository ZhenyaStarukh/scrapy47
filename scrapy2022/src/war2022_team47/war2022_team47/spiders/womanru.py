import scrapy
from scrapy.http import Request
from war2022_team47.items import War2022Team47Item

class WomanruSpider(scrapy.Spider):
    name = 'womanru'
    allowed_domains = ['www.woman.ru']
    start_urls = ['https://www.woman.ru/search/?q=%D1%81%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8&category=0&where=forum&sort=new']
    # start_urls = ['https://www.woman.ru/psycho/socialization/thread/',
    #               'https://www.woman.ru/psycho/medley6/thread/',
    #               'https://www.woman.ru/health/woman-health/thread/',
    #               'https://www.woman.ru/psycho/finance/thread/',
    #               'https://www.woman.ru/psycho/career/thread/']

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request(link_url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2022Team47Item()
        content = response.xpath('//div[@class=\'card-list\']')
        for article_link in content.xpath('.//a'):
            item['discussion_url'] = article_link.xpath('.//@href').extract_first()
            print(item['discussion_url'])
            yield (item)

