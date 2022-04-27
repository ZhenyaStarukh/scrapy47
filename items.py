# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class War2022Team47Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    discussion_url = scrapy.Field()
    discussion_id = scrapy.Field()
    discussion_datetime = scrapy.Field()
    discussion_theme = scrapy.Field()
    discussion_text = scrapy.Field()
    discussion_author_id = scrapy.Field()
    discussion_comments = scrapy.Field()


class ArticleThumbnail(scrapy.Item):
    discussion_url = scrapy.Field()
    discussion_comment_count = scrapy.Field()


class Comment(scrapy.Item):
    comment_id = scrapy.Field()
    comment_disc_id = scrapy.Field()
    comment_author_id = scrapy.Field()
    comment_datetime = scrapy.Field()
    comment_text = scrapy.Field()