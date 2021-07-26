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

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['test']
collection = db['biaoqingbao']


class MongoPipeline(object):
    def process_item(self, item, spider):
        collection.insert_one(dict(item))
        client.close()
        return item


class BiaoqingproPipeline(ImagesPipeline):
    name = ''

    def get_media_requests(self, item, info):
        b_name = item['title']
        self.name = b_name
        yield Request(url=item['url'], dont_filter=False)

    def file_path(self, request, response=None, info=None):
        url = request.url
        print(url)
        file_name = self.name + '.' + url.split('.')[-1]
        print(file_name)
        return file_name

    def item_completed(self, results, item, info):
        print(results)
        return item
