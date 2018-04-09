import pymongo
from mongo_config_test import *

class Save_To_MongoDB(object):
    def __init__(self):
        self.MONGO_URL='localhost'
        self.MONGO_DB='qidiannewbooktest'
        self.MONGO_TABLE='newbookranktest'
        self.client = pymongo.MongoClient(MONGO_URL)
        self.db = self.client[MONGO_DB]

    def save_mongo(self,data):
        if self.db[self.MONGO_TABLE].insert(data):
            print('存储到MongoDB成功', data)
            return True
        return False
