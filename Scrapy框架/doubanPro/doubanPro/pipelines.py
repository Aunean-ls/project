# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.pipelines.images import ImagesPipeline

class DoubanImagesPipeline(ImagesPipeline):
    pass

# class DoubanproPipeline(object):
#     fp = None
#
#     def open_spider(self, spider):
#         print("开始爬虫......")
#         self.fp = open('./douban.txt', 'w', encoding='utf-8')
#
#     def process_item(self, item, spider):
#         title = item['title']
#         age = item['age']
#         director = item['director']
#         screenwriter = item['screenwriter']
#         film_length = item['film_length']
#         country = item['country']
#         language = item['language']
#         type = item['type']
#         to_star = item['to_star']
#         score = item['score']
#         img = item['img']
#         summary = item['summary']
#         # self.fp.write(title + "," + repair_time + "," + price + "," + area + '\n')
#
#         return item
#
#     def close_spider(self, spider):
#         print("结束爬虫！")
#         self.fp.close()


class mysqlPileLine(object):
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host='localhost', user='root', port=3306, password='qaz3357375',
                                    database='spiders')

    def process_item(self, item, spider):
        title = item['title']
        age = item['age']
        director = item['director']
        screenwriter = item['screenwriter']
        film_length = item['film_length']
        country = item['country']
        language = item['language']
        type = item['type']
        to_star = item['to_star']
        score = item['score']
        img = item['img']
        summary = item['summary']
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            'insert into douban("title","age","director","screenwriter","film_length","country","language","type","to_star","score","img","summary") values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (
            title, age, director, screenwriter, film_length, country, language, type, to_star, score, img, summary))
        print("成功")
        self.conn.commit()
        try:
            self.cursor.execute('insert into douban("title","age","director","screenwriter","film_length","country","language","type","to_star","score","img","summary") values("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")' % (title, age, director, screenwriter, film_length, country, language, type, to_star, score, img, summary))
            print("成功")
            self.conn.commit()
            # self.cursor.execute('create table if not exists douban(id int primary key auto_increment, title varchar('
            #                     '1235), '
            #                     'age varchar(1235), director varchar(1235), screenwriter varchar(1235), film_length '
            #                     'varchar(1235), country varchar(1235), language varchar(1235), type varchar(1235), '
            #                     'to_star varchar(1235), score varchar(1235), img varchar(1235),summary varchar(1235))')

        except Exception as e:
            print(f'错误{e}')
            self.conn.rollback()

        return item
