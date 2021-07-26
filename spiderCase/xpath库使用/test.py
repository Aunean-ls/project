# import requests
# from lxml import etree
#
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
# }
#
# url = 'https://changsha.8684.cn/x_24f5dad9'
#
# response = requests.get(url, headers).content.decode('utf-8')
#
# sel = etree.HTML(response)
# time = sel.xpath('//ul[@class="bus-desc"]/li[1]/text()')[0].split('：')[1]
#
# # 参考票价
# price = sel.xpath('//ul[@class="bus-desc"]/li[2]/text()')[0].split('：')[1]
# # 公交公司
# company = sel.xpath('//ul[@class="bus-desc"]/li[3]/a/text()')[0]
# print(time)
# print(price)
# print(company)
# trip1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][1]/div[1]/div[2]/text()')[0]
# total1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][1]/div[2]/div[2]/text()')[0]
# lzList1 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-lzlist mb15"][1]/ol/li/a/text()')
# lzList1 = '->'.join(lzList1)
# print(trip1)
# print(total1)
# print(lzList1)
#
# trip2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][2]/div[1]/div[2]/text()')[0]
# total2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-excerpt mb15"][2]/div[2]/div[2]/text()')[0]
# lzList2 = sel.xpath('//div[@class="layout-left"]//div[@class="bus-lzlist mb15"][2]/ol/li/a/text()')
# lzList2 = '->'.join(lzList2)
# print(trip2)
# print(total2)
# print(lzList2)

d = []
if len(d) == 0:
    print('空的')