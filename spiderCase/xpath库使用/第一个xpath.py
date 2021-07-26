import requests
import csv
from lxml import etree

# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
# }
# url = 'https://www.qiushibaike.com/imgrank/'
# response = requests.get(url, headers).content.decode('utf-8')
# sel = etree.HTML(response)
# img_src = sel.xpath('//div[@class="thumb"]//img/@src')
# for img in img_src:
#     img = 'http:' + img
#     print(img)

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'

}
data_list = []


def crawl(url):
    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    sel = etree.HTML(response)
    tr_list = sel.xpath('//tbody/tr[position()>1]')
    for tr in tr_list:
        data = {
            'rank': tr.xpath('./td[1]/text()')[0],
            'title': tr.xpath('./td[2]/a/text()')[0],
            'hot': tr.xpath('./td[2]/span/text()')[0],
            'detail_url': 'https://s.weibo.com' + tr.xpath('./td[2]/a/@href')[0]
        }

        print(data)
        data_list.append(data)
    save()


def save():
    with open('weibo.csv', 'w', newline='', encoding='utf-8')as f:
        fieldnames = ['rank', 'title', 'hot', 'detail_url']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data_list)


if __name__ == '__main__':
    url = 'https://s.weibo.com/top/summary'
    crawl(url)
