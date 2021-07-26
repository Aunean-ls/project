import requests
from lxml import etree
import csv

# 设置 U-A
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
}
# 存储数据
all_data = []


def crawl(url):
    # 发送HTTP请求，获取响应数据
    response = requests.get(url=url, headers=headers).content.decode('utf-8')
    sel = etree.HTML(response)
    # 获取以数字开头所有路线的信息
    a_list = sel.xpath('//div[@class="bus-layer depth w120"][1]//div[@class="pl10"][1]/div/a')
    # 遍历，一个一个取出
    for a in a_list:
        name = a.xpath('./text()')[0]  # 获取路线开头数字
        href = base_url + a.xpath('./@href')[0]  # 获取具体rul
        response2 = requests.get(url=href, headers=headers).content.decode('utf-8')
        sel = etree.HTML(response2)
        # 获取所有具体路线信息
        a_list2 = sel.xpath('//div[@class="list clearfix"]/a')
        for a2 in a_list2:
            try:
                title = a2.xpath('./@title')[0]  # 取得路线名
                detail_url = base_url + a2.xpath('./@href')[0]  # 获取具体url

                response3 = requests.get(url=detail_url, headers=headers).content.decode('utf-8')
                sel = etree.HTML(response3)
                # 运行时间
                time = sel.xpath('//ul[@class="bus-desc"]/li[1]/text()')[0].split('：')[1]
                # 参考票价
                price = sel.xpath('//ul[@class="bus-desc"]/li[2]/text()')[0].split('：')[1]
                # 公交公司
                company = sel.xpath('//ul[@class="bus-desc"]/li[3]/a/text()')[0]
                # 获取始-终站名
                trip1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][1]/div[1]/div[2]/text()')[0]
                # 获取站数
                total1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][1]/div[2]/div[2]/text()')[0]
                # 获取经过的站名
                lzList1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-lzlist mb15"][1]/ol/li/a/text()')
                lzList1 = '->'.join(lzList1)

                # 判断是否存在
                d = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][2]')
                if len(d) == 0:
                    trip2 = 'null'
                    total2 = 'null'
                    lzList2 = 'null'
                else:
                    trip2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][2]/div[1]/div['
                                      '2]/text()')[0]
                    total2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][2]/div[2]/div['
                                       '2]/text()')[0]
                    lzList2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-lzlist mb15"][2]/ol/li/a/text()')
                    lzList2 = '->'.join(lzList2)

                data = {
                    'title': title,
                    'time': time,
                    'price': price,
                    'company': company,
                    'trip1': trip1,
                    'total1': total1,
                    'lzList1': lzList1,
                    'trip2': trip2,
                    'total2': total2,
                    'lzList2': lzList2,
                }
                print(data)
                all_data.append(data)
            except Exception as e:
                print(e)

    with open('changshaBus.csv', 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['title', 'time', 'price', 'company', 'trip1', 'total1', 'lzList1', 'trip2', 'total2', 'lzList2']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_data)


if __name__ == '__main__':
    # 确定 url
    base_url = 'https://changsha.8684.cn'
    crawl(base_url)
