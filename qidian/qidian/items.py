# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QidianItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # 小说名
    author = scrapy.Field()
    # 作者
    novel_url = scrapy.Field()
    # 小说地址
    novel_status = scrapy.Field()
    # 小说连载状态
    novel_numbers = scrapy.Field()
    # 小说字数
    novel_categroy = scrapy.Field()
    # 小说类别
    name_id = scrapy.Field()
    # 小说编号
    # pass

