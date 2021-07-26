import uuid
import pymysql
import requests
from lxml import etree
import pymongo

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}
all_data = []


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
                    'Id': str(uuid.uuid1()),
                    'traffic_time': traffic_time,
                    'traffic_place': address,
                    'traffic_code': car_code,
                    'traffic_type': car_type,
                    'traffic_behavior': behavior,
                    'traffic_rule': punish_standard
                }
                print(data)
                all_data.append(data)

            except Exception as e:
                print(e)


def insert_data_mongo():
    # 1.连接MongoDB
    client = pymongo.MongoClient(host='localhost', port=27017)

    # 2.指定数据库
    db = client['test']

    # 3.指定集合
    collection = db['TrafficeSafe2']

    # 4.插入多条数据
    collection.insert_many(all_data)


def insert_mysql():

    # 连接database
    conn = pymysql.connect(host='localhost', port=3306,
                           user='root', passwd='qaz3357375',
                           charset='utf8', db='test')
    # 获取操作游标
    cursor = conn.cursor()
    # 表名
    table = 'traffic'

    # 创建表
    sql = 'CREATE TABLE IF NOT EXISTS traffic(' \
          'Id VARCHAR(235) PRIMARY KEY, ' \
          'traffic_time VARCHAR(235), ' \
          'traffic_place VARCHAR(235), ' \
          'traffic_code VARCHAR(235), ' \
          'traffic_type VARCHAR(235), ' \
          'traffic_behavior VARCHAR(235), ' \
          'traffic_rule VARCHAR(235) ' \
          ')CHARSET UTF8'

    cursor.execute(sql)

    data = all_data[0]
    fields = ",".join("`{}`".format(i) for i in data.keys())
    values = ",".join("%({})s".format(i) for i in data.keys())

    # sql = "insert into " + table + "(" + fields + ") values (" + values + ")"
    # print(sql)

    # 第二种
    sql = "insert into " + table + "(%s) values (%s)" % (fields, values)
    # print(sql)

    cursor.executemany(sql, all_data)
    conn.commit()
    print("插入成功")
    cursor.close()
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
    insert_mysql()
    insert_data_mongo()

