import scrapy
import json
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import Comment, War2022Team47Item

class PnpArtSpider(scrapy.Spider):
    name = 'pnpruart'
    allowed_domains = ['www.pnp.ru']


    def start_requests(self):
        data = []
        with open ('./pnpru.json') as json_file:
            data = json.load(json_file)

        for link_url in data:
            print("Url: " + link_url['discussion_url'])
            request = Request(link_url['discussion_url'], cookies={'store_language': 'ru'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2022Team47Item()
        item['discussion_url'] = response.url
        article = response.xpath("//article")
        item['discussion_text'] = "\n".join(article.xpath(".//h1/text()").extract()) \
                                  + "\n\n" + "\n".join(response.xpath(".//div[@class='js-mediator-article']//p/text()").extract())

        yield (item)