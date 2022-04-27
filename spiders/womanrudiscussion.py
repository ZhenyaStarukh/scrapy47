import scrapy
import json
from scrapy.http import Request
from src.war2022_team47.war2022_team47.items import Comment, War2022Team47Item

class WomanruDiscSpider(scrapy.Spider):
    name = 'womanrudiscussion'
    allowed_domains = ['www.woman.ru']


    def start_requests(self):
        base_url = 'https://www.woman.ru'
        data = []
        with open ('./womanru.json') as json_file:
            data = json.load(json_file)

        for link_url in data:
            print("Url: " + link_url['discussion_url'], "Pages", link_url['discussion_comment_count'])
            count = link_url['discussion_comment_count'] // 50
            for page in range(count):
                page_num = ""
                if page > 1:
                    page_num = str(page)
                request = Request(base_url + link_url['discussion_url'] + page_num, cookies={'store_language': 'ru'}, callback=self.parse)
                yield request

    def parse(self, response):
        item = War2022Team47Item()
        item['discussion_url'] = response.url

        item['discussion_id']="_".join([i for i in response.url.split("/") if i.isdigit()])
        print(item['discussion_id'])
        item['discussion_datetime']=response.xpath("//div[@class='card__topic-data']//time/@datetime").extract()
        item['discussion_theme']=response.xpath("//h1[@class='card__topic-title']/text()").extract()
        item['discussion_author_id'] = response.xpath("//div[@class='card card_topic-start']//div[@class='user__metadata']/span/@data-id").extract()
        item['discussion_text'] = "\n".join(response.xpath("//div[@class='card card_topic-start']//div[@class='card__text']//p/text()").extract())
        print(item['discussion_text'])

        comments = list()
        comment_section = response.xpath("//div[@class='card-list']")

        for comment in comment_section.xpath(".//div[@class='card card_answer']"):
            comm = Comment()
            comm['comment_id'] = comment.xpath("./@data-id").extract()
            comm['comment_disc_id'] = comment.xpath("./@data-threadid").extract()
            comm['comment_author_id'] = comment.xpath(".//div[@class='user__metadata']/span/@data-id").extract()
            comm['comment_datetime'] = comment.xpath(".//div[@class='card__message-data']/time/@datetime").extract()
            comm['comment_text'] = comment.xpath(".//p[@class='card__comment']/text()").extract()
            comments.append(comm)
            print(comm['comment_text'])

        item['discussion_comments'] = comments

        yield (item)








