# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class FangtianxiaproPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        address = item['address']
        price = item['price']
        tel = item['tel']

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders2', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'create table if not exists fangtianxia(title varchar(235), ' \
                  'address varchar(235), ' \
                  'price varchar(235), ' \
                  'tel varchar(235))charset utf8'
            cursor.execute(sql)
            sql = 'insert into fangtianxia values("%s", "%s", "%s", "%s")' % (title, address, price, tel)
            cursor.execute(sql)
            print(title+'插入成功')
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return item
