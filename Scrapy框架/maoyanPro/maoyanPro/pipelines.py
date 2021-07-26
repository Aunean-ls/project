# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from maoyanPro.items import MaoyanproItem

# client = pymongo.MongoClient(host='localhost', port=27017)
# db = client['test']
# collection = db['maoyan_2']


# class MaoyanproPipeline(object):
#     def process_item(self, item, spider):
#         print(item)
#         collection.insert_one(dict(item))
#         return item
# import pymysql
# from maoyan import settings
import pymysql
import csv

class MaoyanPipeline(object):
    def process_item(self, item, spider):
        f = open('data.csv', 'a', encoding='utf-8', newline='')
        f.write('电影名,演员,时间,评分' + '\n')
        title = item['title']
        actor = item['actor']
        time = item['time']
        score = item['score']
        data = [title, actor, time, score]
        data = ','.join(data)
        f.write(data + '\n')
        f.close()



        # with open('data.csv', 'a', encoding='utf-8', newline='') as f:
        #     fieldnames = ['title', 'actor', 'time', 'score']
        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
        #     # writer.writeheader()
        #     f.write(data + '\n')

        # # ********** Begin **********#
        # # 1.连接数据库
        # conn = pymysql.connect(
        #     host='localhost',  # 连接的是本地数据库
        #     port=3306,  # 数据库端口名
        #     user='root',  # 自己的mysql用户名
        #     passwd='qaz3357375',  # 自己的密码
        #     db='spiders',  # 数据库的名字
        #     charset='utf8',  # 默认的编码方式
        # )
        # cursor = conn.cursor()
        # try:
        #     sql = 'create table if not exists mymovies(title varchar(235), actor varchar(235), time varchar(235), score varchar(235))charset utf8'
        #     cursor.execute(sql)
        #     # sql = 'insert into mymovies values (\'%s\',\'%s\',\'%s\',\'%s\')' % (name, starts, releasetime, score)
        #     sql = 'insert into mymovies values ("%s","%s","%s","%s")' % (title, actor, time, score)
        #     print(title+"插入成功")
        #     cursor.execute(sql)
        #     conn.commit()
        # except Exception as e:
        #     print(f'错误：{e}')
        # finally:
        #     conn.close()
        # return item
