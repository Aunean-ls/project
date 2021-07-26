import requests
from lxml import etree

# 登陆url
url = 'http://www.jobplus.com.cn/login?backurl=sites/getSiteDetail/798'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Host': 'www.jobplus.com.cn',
    'Origin': 'http://www.jobplus.com.cn',
    'Referer': 'http://www.jobplus.com.cn/login?backurl=sites/getSiteDetail/798',
}
# 获取session对象
session = requests.session()

passwd = input("请输入密码：")
# 构建表单
data = {
    'usertype': '1',
    'username': '1453357375@qq.com',
    'passwd': passwd,
}

response = session.post(url=url, data=data, headers=headers)
print(response.history)
# 个人主页url
url = 'http://www.jobplus.com.cn/myCenter/getMyHeadTop'

response = session.get(url=url, headers=headers).content.decode('utf-8')

sel = etree.HTML(response)
# 获取用户名
name = sel.xpath('//p[@class="user-name"]/a/text()')[0].strip()
print(name)


