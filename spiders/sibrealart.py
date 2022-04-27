import scrapy
import json
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import Comment, War2022Team47Item

class SibrealArtSpider(scrapy.Spider):
    name = 'sibrealart'
    allowed_domains = ['www.sibreal.org']


    def start_requests(self):
        base_url = 'https://www.sibreal.org'
        data = []
        with open ('./sibreal.json') as json_file:
            data = json.load(json_file)

        for link_url in data:
            print("Url: " + link_url['discussion_url'])
            request = Request(base_url + link_url['discussion_url'], cookies={'store_language': 'ru'}, callback=self.parse)
            yield request

    def parse(self, response):
        item = War2022Team47Item()
        item['discussion_url'] = response.url

        item['discussion_text'] = "\n".join(response.xpath("//div[@id='content']//p/text()").extract())

        yield (item)