# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class XiaohuaproPipeline(object):
    def process_item(self, item, spider):
        path = '笑话2/'
        if not os.path.exists(path):
            os.mkdir(path)
        title = item['title']
        content = item['content']
        with open(path+title+'.txt', 'w', encoding='utf-8') as f:
            f.write(content + '\t')
        return item
