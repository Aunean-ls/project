import requests
from lxml import etree
import pymongo

all_content = []
# 设置U-A和Cookie
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
    'Cookie': 'c_csrf=df2c67ee-1d1b-4262-b743-ebf057acffd3; _bl_uid=FekmOnO25j9t5hbp7wevxym53L4p; aliyun_lang=zh; aliyunAliothSource=eyJzcG0iOiI1MTc2LjE5NzIwMjU4LkpfMjkzNzMzMzU0MC5kNDAyIiwic2NtIjoiMjAxNDA3MjIuQl8xNDE0LlBfMzQ2NC5NT180MDItU1RfMzYzNi1JRF8yMTY5Ny1DSURfMjE2OTctVl8xIn0=; ping_test=true; t=f584beea75c4218addd6fd5879160bbf; _tb_token_=e73b5bde34d5f; cookie2=1baae834e5d422da0abeb256589173ea; _samesite_flag_=true; login_aliyunid_pk=1337602563736547; FECS-XSRF-TOKEN=7fdd4cb1-263a-4251-ad16-2b4b68056114; UC-XSRF-TOKEN=a96ab3fd-abd9-42dc-8596-ee57074fbfb5; aliyunMerakSource=WyJkY2RucGF5YmFnLjEyMDMxODAuMzczNjA2OTIxLm5vbi4yMDE0MDcyMnxNXzQ0NTM3OHxffFZfMS40NDUzNzguIiwic2Nkbi4uLm5vbi4uLiJd; console_base_assets_version=3.27.1; aliyun_choice=CN; env=prod; host=beian.aliyun.com; aliyun_beian_reqUrl=https://m-beian.aliyun.com; currentRegionId=cn-hangzhou; FECS-UMID=%7B%22token%22%3A%22Y1106db4d5fcd8393b2bd935462e67b94%22%2C%22timestamp%22%3A%224954765855555C44564F6075%22%7D; JSESSIONID=4564BDFF2D047A91BBEA308DF66A85CC; login_aliyunid="au****"; login_aliyunid_ticket=OTwChTBoNM1ZJeedfK9zxYnbN5hossqIZCr6t7SGxRigm2Cb4fGaCdBZWIzmgdHq6sXXZQg4KFWufyvpeV*0*Cm58slMT1tJw3_5$$XdUXdZyyzhI_v0IawcZqvoxg8VSsCQYctbhTE6sEtyof_BNp_U0; login_aliyunid_luid="BG+uzev159N9841f610c923c3475eede63513f84778+RY61oMDa3yW79SwjhtPnVQ=="; login_aliyunid_csrf=_csrf_tk_1119018832507812; login_aliyunid_abi="BG+rD5GlZJc7961c0393e56850360bd65ed39da7806+g3o/YAQ3h2PxbNl7LVbvzRStttknnKRTzwAvcjoq7pNN+QaYuLI="; login_aliyunid_pks="BG+/rSIi4TURl1gHIIP+jXlTLuuf7NhlJrXZUOsweCVCvw="; hssid=93187f25-c458-4efc-b0ad-0c2e4152aaf7; hsite=6; aliyun_country=CN; aliyun_site=CN; isg=BBQUwzOYCLpG-5xneQIPyXMu5VKGbThXWvpd-K71oB8imbTj1n0I58oYmZEBYXCv; l=eBPV3pccjHaTxqWJBOfwourza77OSIRAguPzaNbMiOCP9i5B5uTNW6aIhUY6C3GVhsNHR3yIziz8BeYBqQd-nxvTkjOadJMmn; tfstk=cVY1BdA9ZR2sFxm47CGUuHRssEQAa_kCtc69136_zEOZwrRNpsf0zT1Usn23JgCC.'
}
# 确定url
base_url = 'https://developer.aliyun.com/group/bigdata?spm=a2c6h.13528211.0.0.59164307S4njo5#/?_k=8ma2ot'

response = requests.get(url=base_url, headers=headers).content.decode('utf-8')
sel = etree.HTML(response)

# 获得所有文章具体链接
href_list = sel.xpath('//ul[@class="content-tab-list article-list show"]/li/a/@href')
for href in href_list:
    href = 'https://developer.aliyun.com' + href
    response2 = requests.get(url=href, headers=headers).content.decode('utf-8')
    sel = etree.HTML(response2)
    # 获取文章标题
    title = sel.xpath('//div[@class="content-wrapper"]/h1/text()')[0]
    # 获取作者名
    author = sel.xpath('//p[@class="article-info"]/a/text()')[0]
    # 获取文章发布时间
    time = sel.xpath('//span[@class="article-info-time"]/text()')[0]
    # 获取文章正文
    content = sel.xpath('//div[@class="content-wrapper"]/div//text()')
    content = ''.join(content).strip()

    data = {
        'title': title,
        'author': author,
        'time': time,
        'content': content
    }
    print(data)
    all_content.append(data)

# 1.连接MongoDB
client = pymongo.MongoClient(host='localhost', port=27017)

# 2.指定数据库
db = client['test']

# 3.指定集合
collection = db['aliyun']

# 4.插入多条数据
collection.insert_many(all_content)

# 查询一条数据
find_one = collection.find_one()
# print(find_one)

# 查询所有数据
all_data = collection.find()
for d in all_data:
    print(d)

# 更新数据
update_one = collection.update_one(
    {'author': '赛道明星-沈铭洲'},
    {'$set': {'title': '大数据文章'}}
)
data_result = collection.find_one({'author': '赛道明星-沈铭洲'})
print(data_result)
print('-'*50)
# # 删除数据
collection.delete_many({'author': '赛道明星-沈铭洲'})
all = collection.find()
for a in all:
    print(a)
