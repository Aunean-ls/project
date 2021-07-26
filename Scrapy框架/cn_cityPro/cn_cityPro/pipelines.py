# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo


class CnCityproPipeline(object):
    def process_item(self, item, spider):
        # try:
        #     client = pymongo.MongoClient(host='localhost', port=27017)
        #     db = client['test']
        #     collection = db['cn_city']
        #     collection.insert_one(dict(item))
        #     print('成功')
        # except Exception as e:
        #     print(e)
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders2', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'create table if not exists cn_city(' \
                  'location_id varchar(235), ' \
                  'city_name varchar(235), ' \
                  'country_name varchar(235), ' \
                  'adm1 varchar(235), ' \
                  'adm2 varchar(235), ' \
                  'latitude varchar(235), ' \
                  'longitude varchar(235), ' \
                  'code varchar(235)' \
                  ')charset utf8'
            cursor.execute(sql)
            keys = ','.join(item.keys())
            values = ','.join(['%s'] * len(item))
            sql = 'insert into cn_city({keys}) values({values})'.format(keys=keys, values=values)
            cursor.execute(sql, tuple(item.values()))
            print('successful')
            conn.commit()
        except Exception as e:
            print(e)

        finally:
            conn.close()
