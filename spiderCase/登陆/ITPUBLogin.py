import requests
from lxml import etree

# 登陆url
url = 'http://account.itpub.net/login/login?url=undefined'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://account.itpub.net/login/',
    'Host': 'account.itpub.net',
    'Accept': 'application/json, text/javascript, */*; q=0.01'
}
# 获取session对象
session = requests.session()

# response = requests.get(url=url, headers=headers).content.decode('utf-8')
# sel = etree.HTML(response)
# token = sel.xpath('//input[@name="_token"]/@value')[0]
data = {
    'username': 'Aunean',
    'password': 'qaz3357375',
    '_token': 'pZIyhVGYYZcYs9kB82HQ7OnUkM8n6BcDOk7BucY3',
}

response = session.post(url=url, data=data, headers=headers)
print(response.text)

# 个人主页url
url = 'http://account.itpub.net/ucenter/user/index'
response = session.get(url=url, headers=headers).text
sel = etree.HTML(response)
# 获取用户手机号
phone = sel.xpath('//div[@class="form-item"]/div/span[1]/text()')[0].strip()
print(phone)


