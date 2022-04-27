import scrapy
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import ArticleThumbnail


class WomanruSpider(scrapy.Spider):
    name = 'womanru'
    allowed_domains = ['www.woman.ru']
    start_urls = ['https://www.woman.ru/search/?q=%D1%81%D0%B0%D0%BD%D0%BA%D1%86%D0%B8%D0%B8&category=0&where=forum&sort=new']

    def start_requests(self):
        for link_url in self.start_urls:
            print(link_url)
            request = Request(link_url, cookies={'store_language': 'en'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = ArticleThumbnail()
        content = response.xpath('//div[@class=\'card-list\']')
        for article_link in content.xpath(".//h2//a"):
            item['discussion_url'] = article_link.xpath('./@href').extract_first()
            item['discussion_comment_count'] = int(article_link.xpath("./span[@class='card__metadata']/text()")\
                .extract_first().split(" ")[0])

            print(item['discussion_url'])
            yield (item)

