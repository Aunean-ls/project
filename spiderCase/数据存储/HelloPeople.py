import pymongo
import requests
from lxml import etree


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}
all_content = []


def crawle(url):
    # 步骤二：发送 HTTP 请求
    # 步骤三：获取响应数据
    response = requests.get(url=url, headers=headers).content.decode('gbk')

    # 步骤四：数据解析
    sel = etree.HTML(response)

    # 获取详情页
    href_list = sel.xpath('//ul[@class="list_16 mt10"]/li/a/@href | //ul[@class=" list_16 mt10"]/li/a/@href')
    for href in href_list:
        detail_url = 'http://opinion.people.com.cn' + href

        detail_response = requests.get(url=detail_url, headers=headers).content.decode('gbk')
        sel = etree.HTML(detail_response)
        # 新闻标题
        title = sel.xpath('//h1/text()')[0].strip().replace('\xa0', '')
        # 作者
        author = sel.xpath('//div[@class="author cf"]/text() | //p[@class="author"]/text()')[0].replace('\xa0', '')
        # 时间
        time = sel.xpath('//div[@class="channel cf"]/div/text()[1] | //div[@class="box01"]/div[@class="fl"]/text()')[0].split()[0].strip()
        # 内容
        content = sel.xpath('//div[@class="rm_txt_con cf"]/p/text() | //div[@class="box_con"]/p/text()')
        content = ''.join(content).strip().replace('\n\t', '')

        data = {
            'title': title,
            'author': author,
            'time': time,
            'content': content,
        }
        print(data)
        all_content.append(data)
    insert_data_mongo()


def insert_data_mongo():
    # 1.连接MongoDB
    client = pymongo.MongoClient(host='localhost', port=27017)

    # 2.指定数据库
    db = client['test']

    # 3.指定集合
    collection = db['HelloPeople']

    # 4.插入多条数据
    collection.insert_many(all_content)


if __name__ == '__main__':
    # 步骤一：确定url
    url_list = ['http://opinion.people.com.cn/GB/427456/434886/index{}.html'.format(i) for i in range(1, 2)]
    for url in url_list:
        crawle(url)



