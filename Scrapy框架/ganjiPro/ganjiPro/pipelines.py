# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class GanjiproPipeline(object):
    def process_item(self, item, spider):
        company_name = item['company_name']
        company_type = item['company_type']
        company_industry = item['company_industry']
        company_size = item['company_size']
        company_introduction = item['company_introduction']
        position = item['position']
        salary = item['salary']
        level = item['level']
        number_recruiters = item['number_recruiters']
        work_location = item['work_location']
        update_time = item['update_time']

        conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', db='spiders2', charset='utf8')
        cursor = conn.cursor()
        try:
            sql = 'create table if not exists ganji(' \
                  'company_name varchar(235), ' \
                  'company_type varchar(235), ' \
                  'company_industry varchar(235), ' \
                  'company_size varchar(235), ' \
                  'company_introduction varchar(235), ' \
                  'position varchar(235), ' \
                  'salary varchar(235), ' \
                  'level varchar(235), ' \
                  'number_recruiters varchar(235), ' \
                  'work_location varchar(235), ' \
                  'update_time varchar(235))charset utf8'
            cursor.execute(sql)
            sql = "insert into ganji values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            company_name, company_type, company_industry, company_size, company_introduction, position, salary, level,
            number_recruiters, work_location, update_time)
            cursor.execute(sql)
            conn.commit()
            print('成功', company_name)
        except Exception as e:
            print(e)
        finally:
            conn.close()
        return item
