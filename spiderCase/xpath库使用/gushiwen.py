import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
url = 'https://so.gushiwen.org/shiwenv_a1e7559dada7.aspx'

response = requests.get(url, headers).content.decode('utf-8')
sel = etree.HTML(response)

# 古诗名
title = sel.xpath('//h1/text()')[0]

# 作者
author = sel.xpath('//*[@id="sonsyuanwen"]/div[1]/p/a/text()')[0]

# 内容
contents = sel.xpath('//div[@id="contsona1e7559dada7"]/text()')
print(title)
poem = ''
print(author)
for content in contents:
    content = content.strip()
    poem = poem+content+"\n"
with open(title+'.txt', 'w', encoding='utf-8')as f:
    f.write(title+'\n'+author+'\n'+poem)
print(poem)

