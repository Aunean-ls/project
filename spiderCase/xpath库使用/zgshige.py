import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
url = 'http://www.zgshige.com/c/2020-12-11/16138627.shtml'

response = requests.get(url, headers, timeout=10).content.decode('gbk')
sel = etree.HTML(response)
title = sel.xpath('//h3/text()')[0]
author = sel.xpath('//div[@class="col-xs-12"]/span[1]/text()')[0]

contents = sel.xpath('//*[@id="content"]/div[2]/p[2]/text()')
print(title)
poem = ''
author = author.replace('\n', '').replace('\t', '')
print(author)
for content in contents:
    content = content.strip()
    poem = poem+content+"\n"
with open(title+'.txt', 'w', encoding='utf-8')as f:
    f.write(title+'\n'+author+'\n'+poem)
print(poem)
