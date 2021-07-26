import requests
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}


def stripText(textList):
    # //将文本列表转化成字符串，并去掉其中包括的/n /t /r /等字符串
    # :param textList 文本列表
    # :return:字符串

    str_list = ""
    for item in textList:
        item_str = item.replace('\n', "").replace('\r', "").replace('\t', "").replace('/', "").replace('-', "")
        # item_str = item.strip() #当参数为空时，默认删除字符串两端的空白字符（包括'\n','\r','\t','')
        if item_str != '':
            if str_list != '':
                str_list = str_list + "," + item_str
            else:
                str_list = item_str
        return str_list


def crawl(url):
    response = requests.get(url, headers).content.decode('utf-8')
    print(response)
    sel = etree.HTML(response)
    div_list = sel.xpath('//div[@class="list fl"]/div[@class="items"]/div')

    for div in div_list:
        name = div.xpath('./div[2]/div/span/a/text()')[0].strip()
        price = div.xpath('./div[2]/div[2]/div[2]/div/text()')[0].strip()
        address = div.xpath('./div[2]/div[2]/div/div/div/a/text()')[0].strip()
        type = div.xpath('./div[2]/div[2]/div[1]/div[2]/a/text()')[0].strip()

        data = name + ',' + price + ',' + address + ',' + type
        print(data)
        with open('HelloFang_搜房.txt', 'a', encoding='utf-8') as f:
            f.write(data + '\n')


if __name__ == '__main__':
    url_list = ['https://cs.sofang.com/new/area/aa999-bl{}?'.format(i) for i in range(1, 2)]
    for url in url_list:
        crawl(url)
