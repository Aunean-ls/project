import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}


def crawl(url):
    response = requests.get(url, headers).content.decode('gbk')
    sel = etree.HTML(response)
    li_list = sel.xpath('//*[@id="newhouse_loupai_list"]/ul/li')

    for li in li_list:
        name = li.xpath('.//*[@class="nlcd_name"]/a/text()')[0].strip()
        price = li.xpath('.//div[@class="nhouse_price"]/span/text()')[0]
        address = li.xpath('.//div[@class="address"]/a/@title')[0].strip()
        area = li.xpath('.//*[@class="house_type clearfix"]/text()[last()]')[0].replace('－', '').strip()

        data = name + ',' + price + ',' + address + ',' + area
        print(data)
        with open('newhouse.txt', 'a', encoding='utf-8') as f:
            f.write(data+'\n')


if __name__ == '__main__':
    url_list = ['https://cs.newhouse.fang.com/house/s/b9{}/'.format(i) for i in range(1, 2)]
    for url in url_list:
        crawl(url)
