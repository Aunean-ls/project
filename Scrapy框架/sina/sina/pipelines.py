# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class SinaPipeline:

    def open_spider(self,spider):
        self.db = pymysql.connect(
            host='localhost',port=3306,
            user='root',password='tys1109tys',
            database='spider88',charset='utf8'

        )
        self.cursor = self.db.cursor()

    #爬虫结束
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

    def process_item(self, item, spider):
        print(spider.name)
        # print(f'-----{item}-----')
        #sql语句
        news_title = item['newstitle']
        news_time = item['newstime']

        sql = 'insert into sinanews(newstitle, newstime) values("%s","%s")' % (news_title,news_time)

        self.cursor.execute(sql)
        self.db.commit()

        return item

