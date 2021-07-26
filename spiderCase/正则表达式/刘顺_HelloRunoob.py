import re
import requests

url = 'https://www.runoob.com/'
headers = {
       'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'

}
response = requests.get(url=url, headers=headers).content.decode('utf-8')
title = re.findall('<title>(.*?)</title>', response)[0]
a_list = re.findall('<a.*?>(.*?)</a>', response)
print(title)
for a in a_list:
    print(a)
