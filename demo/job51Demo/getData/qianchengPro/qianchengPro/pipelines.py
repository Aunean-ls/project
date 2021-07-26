# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors


class QianchengproPipeline(object):

    def __init__(self):
        self.file = open('../../../data/originalData.csv', 'w', newline='', encoding='utf-8')
        self.csvwriter = csv.writer(self.file)
        self.csvwriter.writerow(['岗位名称', '公司名称', '工作地点', '薪资', '工作福利', '公司类型', '招聘人数',
                                 '工作经验', '发布日期', '公司规模', '招聘详情'])

    def process_item(self, item, spider):
        self.csvwriter.writerow([item["jobName"], item["companyName"], item["workArea"], item["salary"],
                                 item['welfare'], item['companyType'], item['degreeFrom'], item['workYear'],
                                 item['issueDate'], item['companySize'], item['jobHref']])
        return item

    def close_spider(self, spider):
        self.file.close()


class mysqlPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        # print(item)
        table = 'jobInfo'
        keys = ','.join(item.keys())
        values = ','.join(['%s'] * len(item))
        insert_sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)

        cursor.execute(insert_sql, tuple(item.values()))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)
