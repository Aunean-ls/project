import requests
from lxml import etree
import pymongo

all_content = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}

base_url = 'https://mongoing.com/zhangyaogxing'

response = requests.get(url=base_url, headers=headers).content.decode('utf-8')
sel = etree.HTML(response)

# 获得所有文章具体链接
href_list = sel.xpath('//div[@class="content"]/article/header//a/@href')
for href in href_list:
    response2 = requests.get(url=href, headers=headers).content.decode('utf-8')
    sel = etree.HTML(response2)
    # 获取文章标题
    title = sel.xpath('//h1/a/text()')[0]
    # 获取文章发布时间
    time = sel.xpath('//div[@class="article-meta"]/span[1]/text()')[0]
    # 获取文章正文数据
    content = sel.xpath('//article[@class="article-content"]//text()')
    content = ''.join(content).strip()

    data = {
        'title': title,
        'time': time,
        'content': content
    }
    # print(data)
    all_content.append(data)

# 1.连接MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
db = client['test']

# 3.指定集合
collection = db['Mongoing']

# 4.插入多条数据
collection.insert_many(all_content)

# 并对存储的数据进行查询、更新和删除操作（2 +）
# 查询一条数据
find_one = collection.find_one()
print(find_one)

# 查询所有数据
all_data = collection.find()
print(all_data)

# 更新数据
update_one = collection.update_one(
    {'time': '2021-03-01'},
    {'$set': {'title': '并发数'}}
)
data_result = collection.find_one({'time': '2021-03-01'})
print(data_result)

# 删除数据
collection.delete_many({'time': '2021-03-01'})
all = collection.find()
for a in all:
    print(a)
