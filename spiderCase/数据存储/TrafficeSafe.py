import csv
import uuid
import pymysql
import pymongo
import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}
all_content = []


def crawl(url):
    # 步骤二：发送 HTTP 请求
    # 步骤三：获取响应数据
    response = requests.get(url=url, headers=headers).content.decode('utf-8')

    # 步骤四：数据解析
    sel = etree.HTML(response)

    # 获取详情页
    href_list = sel.xpath('//div[@class="info_list_top"]/a/@href')
    for href in href_list:

        detail_response = requests.get(url=href, headers=headers).content.decode('utf-8')
        sel = etree.HTML(detail_response)

        tr_list = sel.xpath('//div[@class="article_content"]//tbody/tr[position()>1]')

        for tr in tr_list:

            d_len = len(tr.xpath('./td'))
            try:
                if d_len == 7 or d_len == 6:
                    # if d_len > 5:
                    # 违法时间
                    traffic_time = tr.xpath('./td[last()-5]//text()')[0].replace('\xa0', '')
                    # 违法地点
                    address = tr.xpath('./td[last()-4]//text()')[0].replace('\xa0', '')
                    # 车牌号码
                    car_code = tr.xpath('./td[last()-3]//text()')
                    car_code = ''.join(car_code).strip()
                    # 车辆类型
                    car_type = tr.xpath('./td[last()-2]//text()')[0]
                    # 违法行为
                    behavior = tr.xpath('./td[last()-1]//text()')[0]
                    # 处罚标准
                    punish_standard = tr.xpath('./td[last()]//text()')[0]

                else:
                    # 违法时间
                    traffic_time = tr.xpath('./td[1]//text()')[0].replace('\xa0', '')
                    # 违法地点
                    address = tr.xpath('./td[3]//text()')[0].replace('\xa0', '')
                    # 车牌
                    car_code = tr.xpath('./td[2]//text()')
                    car_code = ''.join(car_code).strip()
                    # 车辆类型
                    car_type = "暂无信息"
                    # 违法行为
                    behavior = tr.xpath('./td[4]//text()')[0]
                    # 处罚
                    punish_standard = tr.xpath('./td[5]//text()')[0]

                data = {
                    'traffic_time': traffic_time,
                    'address': address,
                    'car_code': car_code,
                    'car_type': car_type,
                    'behavior': behavior,
                    'punish_standard': punish_standard
                }
                print(data)
                all_content.append(data)
                insert_data_mysql(data)

            except Exception as e:
                print(e)

    # insert_data_mongo()


def insert_data_mongo():
    # 1.连接MongoDB
    client = pymongo.MongoClient(host='localhost', port=27017)

    # 2.指定数据库
    db = client['test']

    # 3.指定集合
    collection = db['TrafficeSafe2']

    # 4.插入多条数据
    collection.insert_many(all_content)


def insert_data_mysql(data):
    # 1.连接数据库
    conn = pymysql.connect(host='localhost', user='root', password='qaz3357375', port=3306, db='crawler',
                           charset='utf8')
    cursor = conn.cursor()

    # 2.创建表
    sql = 'CREATE TABLE IF NOT EXISTS trafficSafety(' \
          'id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, ' \
          'traffic_time VARCHAR(235), ' \
          'address VARCHAR(235), ' \
          'car_code VARCHAR(235), ' \
          'car_type VARCHAR(235), ' \
          'behavior VARCHAR(235), ' \
          'punish_standard VARCHAR(235) ' \
          ')CHARSET UTF8'

    cursor.execute(sql)

    # 3.插入数据
    table = 'trafficSafety'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'INSERT INTO {table}({keys}) VALUES({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print('Successful')
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    # 关闭连接
    conn.close()


end_page = int(input('请输入结束页：'))

if __name__ == '__main__':
    # 步骤一：确定url
    for i in range(1, end_page + 1):
        if i <= 3:
            url_list = ['http://csga.changsha.gov.cn/jjzd/csjj_index/topic_4169_{}.shtml'.format(i)]
            for url in url_list:
                crawl(url)

        else:
            url_list = ['http://csga.changsha.gov.cn/jjzd/csjj_index/pagemore_4169.shtml?topicId=4169&pageSize=15'
                        '&page={}'.format(i)]
            for url in url_list:
                crawl(url)
