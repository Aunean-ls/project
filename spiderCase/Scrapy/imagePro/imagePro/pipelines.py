# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
from scrapy.http import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class MongoPipeline(object):

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[spider.name].insert(dict(item))
        # print('数据库中集合的名字：' + spider.name)
        return item

    def close_spider(self, spider):
        self.client.close()


class ImageproPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(url=item['url'], dont_filter=False)   # dont_filter=False是否去重

    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url
        print(url)
        file_name = url.split('/')[-1]
        print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        # print(results)
        return item
