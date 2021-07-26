import requests


url = 'https://passport.fang.com/login.api'

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'https://passport.fang.com/?backurl=http%3a%2f%2fmy.fang.com%2f',
    'Accept-Language': 'zh-Hans-CN,zh-Hans;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'passport.fang.com'
}

data = {
    'AutoLogin': '0',
    'pwd': '0be3b03ba383aca8a74ec6b8758033561e388fda76bb8830958d54c5ab14f70f5c5842b2843352a17d10f632dbc7fcdf73c2e0e69815bbc390cf7fa4630c69d12abb51f153aac4282bca55e0b1e1e62c75c71f832a3e1e1ae6d3cb58349588e23f2986bec7a556a20b3c419a7d99bc0468ddf046bba754095662ad828d37556f',
    # 'AutoLogin': '1',
    # 'pwd': '0d9c1c74250c41d0826302fed6cbfce279ad2d8b81a3f67238bfdfb7173e02dd990c8db7731dfdc124190281fcd825f51943b738744a19743b357dec7133e89792bfc559dc581ea30136f9362955130da9f8f339128cc3c03384735367cfe4a004290f1e6fc005b84ebda9b1b9666e0c68940cd0ed6cce40ba7b5ffff3134fc6',
    'Service': 'soufun-passport-web',
    'uid': '13272436629'
}

session = requests.session()

response = session.post(url=url, headers=headers, data=data)
response.encoding = response.apparent_encoding

html_content = response.text
print(response.status_code)
print(html_content)

# url = 'https://my.fang.com/'
#
# response = session.get(url=url, headers=headers, data=data)
# print(response.text)
# with open('FangLogin.html', 'w', encoding='utf-8') as f:
#     f.write(html_content)





