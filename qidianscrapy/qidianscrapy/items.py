# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank = scrapy.Field()
    cate = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    freshtime = scrapy.Field()