import csv
import requests
from lxml import etree

# 步骤一：确定url
base_url = 'http://www.stats.gov.cn/tjfw/sxqygs/gsxx/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}

# 存储数据
all_content = []


def crawle(url):
    # 步骤二：发送 HTTP 请求
    # 步骤三：获取响应数据
    response = requests.get(url=url, headers=headers).content.decode('utf-8')

    # 步骤四：数据解析
    sel = etree.HTML(response)

    # 获取详情页
    href_list = sel.xpath('//ul[@class="center_list_contlist"]/li/a/@href')

    for href in href_list:
        detail_url = base_url + href.replace('./', '')

        detail_response = requests.get(url=detail_url, headers=headers).content.decode('utf-8')
        sel = etree.HTML(detail_response)

        # 企业名称
        name = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[1]/td[2]/p/span/text()')[0]

        # 地址
        address = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[2]/td[2]/p/span/text()')[0]

        # 统一社会信用代码
        code = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[3]/td[2]/p/span/text()')[0].strip()

        # 法定代表人姓名
        person = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[5]/td[2]/p/span/text()')[0]

        # 违法事实
        reason = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[7]/td[2]/p/span/text()')[0]

        # 处罚类别1
        deal1 = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[8]/td[2]/p/span/text()')[0]

        # 处罚类别2
        deal2 = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[9]/td[2]/p/span/text()')
        deal2 = ''.join(deal2)

        # 处罚决定日期
        deal_date = sel.xpath('//table[@class="MsoNormalTable"]/tbody/tr[13]/td[2]/p/span/text()')[0]

        content = {
            'name': name,
            'address': address,
            'code': code,
            'person': person,
            'reason': reason,
            'deal1': deal1,
            'deal2': deal2,
            'deal_date': deal_date
        }
        print(content)
        all_content.append(content)


def save_data():
    # 步骤五：存储数据
    with open('chengxin_统计局.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['name', 'address', 'code', 'person', 'reason', 'deal1', 'deal2', 'deal_date']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_content)


end_page = input('请输入结束页：')

if __name__ == '__main__':
    for p in range(0, int(end_page)):
        if p == 0:
            url = base_url + 'index.html'
        else:
            page = str(p)
            url = base_url + 'index_' + page + '.html'
        crawle(url)
    save_data()

