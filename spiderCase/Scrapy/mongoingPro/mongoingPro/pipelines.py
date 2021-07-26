# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test']
collection = db['mongoing']


class MongoingproPipeline:
    def process_item(self, item, spider):
        collection.insert_one(dict(item))
        return item
