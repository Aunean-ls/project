# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class LianjiaproPipeline(object):
    fp = None

    def open_spider(self, spider):
        print("开始爬虫......")
        self.fp = open('./lianjia.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        title = item['title']
        repair_time = item['repair_time']
        price = item['price']
        area = item['area']
        self.fp.write(title + "," + repair_time + "," + price + "," + area + '\n')

        return item

    def close_spider(self, spider):
        print("结束爬虫！")
        self.fp.close()


class mysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', user='root', port=3306, password='qaz3357375',
                                    database='spiders')

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into lianjia values("%s", "%s", "%s", "%s")' % (item["title"], item['repair_time'], item['price'], item['area']))
            self.conn.commit()
        except Exception as e:
            print(f'错误{e}')
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
