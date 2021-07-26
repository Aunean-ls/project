import requests

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Referer': 'https://www.educoder.net/',
}
url = 'https://data.educoder.net/api/accounts/login.json'
data = {
    'autologin': 'true',
    'login': "13272436629",
    'password': "qaz3357375"
}

session = requests.session()

response = session.post(url=url,headers=headers,data=data)
response.encoding = response.apparent_encoding

html_content = response.text
print(response.status_code)
print(html_content)
with open('DoubanLogin.html', 'w', encoding='utf-8') as f:
    f.write(html_content)


# url = 'https://accounts.douban.com/j/mobile/login/basic'
# s = requests.session()
# print(s.cookies.get_dict())
#
# res = s.get(url, stream=True)
# data = {
#     'ck': '',
#     'remember': 'true',
#     'name': '13272436629',
#     'password': 'qaz3357375',
# }
#
# rs = s.post(url=url, headers=headers)
# print(rs.cookies)
#
# c = requests.cookies.RequestsCookiesJar()
# s.cookies.update(c)
# print(s.cookies.get_dict())




