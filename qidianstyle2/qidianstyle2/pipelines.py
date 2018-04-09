# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings


class Qidianstyle2Pipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        client = pymongo.MongoClient(host=host, port=port)
        dbName = settings['MONGODB_DB']
        tdb = client[dbName]
        self.post = tdb[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        movie_info = dict(item)
        self.post.insert(movie_info)
        return item