import requests
from lxml import etree

url = 'https://github.com/session'

# 设置全局变量U-A
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
session = requests.session()

response = session.post(url=url, headers=headers).content.decode('utf-8')
sel = etree.HTML(response)
token = sel.xpath('//form/input[@name="authenticity_token"]/@value')
print(token)

data = {
    'commit': 'Sign in',
    'authenticity_token': token[0],
    'login': '1453357375@qq.com',
    'password': 'qaz3357375',
    'trusted_device': '',
    'webauthn-support': 'supported',
    'webauthn-iuvpaa-support': 'supported',
    'return_to': '',
    'allow_signup': '',
    'client_id': '',
    'integration': '',
    'required_field_baba': '',
}

response = session.post(url=url, data=data, headers=headers)
print(response.history)


url = 'https://github.com/'
response2 = session.post(url=url, data=data, headers=headers).content.decode('utf-8')
print(response2)

sel = etree.HTML(response)
# 获取用户名
warehouse_names = sel.xpath('//div[@class="mb-3 Details js-repos-container mt-5"]//ul[@class="list-style-none"]/li/div/a/span[2]/text()')
for name in warehouse_names:
    print(name)









