import json
import requests
from bs4 import BeautifulSoup

# 步骤一：确定 url
url = 'https://juejin.cn/post/6947143639373971464'
data = []
# 设置 U-A
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}

# 步骤二三：发送HTTP请求，获取响应数据
response = requests.get(url, headers).content.decode('utf-8')

# 步骤四：数据解析
# 构建bs4对象
soup = BeautifulSoup(response, 'lxml')

title = soup.title.string
print(str(title))
# 文章时间 time标签 datetime属性值
time = soup.time.attrs['datetime']
print(str(time))

# 文章的标题
article_title = soup.find('h1', class_='article-title').text.strip()
print(article_title)

# 文章的内容
article_content = soup.find('div', class_='article-content').find_all_next('p')
# print(article_content)

article_p = ''

for p in article_content:
    article_p += p.text
print(article_p)

# 步骤五：对数据进行持久化
content = {
    '网页标题': title,
    '发布时间': time,
    '文章标题': article_title,
    '文章内容': article_p
}
data.append(content)
# 存储为 txt 文本
# with open('juejin.txt', 'w', encoding='utf-8') as f:
#     f.write(str(content))

# 存储为 json 文本
with open('juejin.josn', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False, indent=2))
