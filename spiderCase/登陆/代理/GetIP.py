import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}

all_content = []
urls = ['https://www.kuaidaili.com/free/intr/{}/'.format(i) for i in range(10, 30)]
for url in urls:

    response = requests.get(url=url, headers=headers).content.decode('utf-8')

    sel = etree.HTML(response)

    tr_list = sel.xpath('//tbody/tr')
    for tr in tr_list:
        ip = tr.xpath('./td[1]/text()')[0]
        port = tr.xpath('./td[2]/text()')[0]
        type_ = tr.xpath('./td[4]/text()')[0]

        ip_port = ip+":"+port

        data = {
            type_: ip_port
        }
        all_content.append(data)
print(all_content)





