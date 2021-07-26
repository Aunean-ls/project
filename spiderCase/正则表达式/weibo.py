import re
import requests

url = 'https://s.weibo.com/top/summary'
headers = {
       'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'

}
response = requests.get(url=url, headers=headers).content.decode('utf-8')
content_list = re.findall('<td class=".*?target="_blank">(.*?)</a>.*?</td>', response, re.S)
hot = re.findall('<span>(.*?)</span>', response, re.S)

# for content in content_list:
#     print(content)
print(hot)
