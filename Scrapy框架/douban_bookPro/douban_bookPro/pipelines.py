# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class DoubanBookproPipeline(object):

    def process_item(self, item, spider):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders2')
        cursor = conn.cursor()
        try:
            sql = 'create table if not exists book(' \
                  'ISBN varchar(235), ' \
                  'title varchar(235), ' \
                  'author varchar(235), ' \
                  'score varchar(235), ' \
                  'price varchar(235), ' \
                  'page varchar(235), ' \
                  'time varchar(235), ' \
                  'press varchar(235), ' \
                  'translator varchar(235), ' \
                  'binding varchar(235), ' \
                  'comments varchar(235), ' \
                  'link varchar(235), ' \
                  'img_url varchar(235)' \
                  ')charset utf8'
            cursor.execute(sql)
            keys = ','.join(item.keys())
            values = ','.join(['%s'] * len(item))

            sql = 'insert into book({keys}) values({values})'.format(keys=keys, values=values)
            cursor.execute(sql, tuple(item.values()))
            conn.commit()
        except Exception as e:
            print(e)

        finally:
            conn.close()
        return item
