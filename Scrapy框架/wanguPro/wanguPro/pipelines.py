# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class WanguproPipeline(object):
    def process_item(self, item, spider):
        path = '万古神帝/'
        if not os.path.exists(path):
            os.mkdir(path)
        title = item['title']
        title = title.replace('?', '？')
        content = item['content']
        print(f'{title} 写入成功')
        with open(path + title + '.txt', 'w', encoding='utf-8') as f:
            f.write(content)
        return item
