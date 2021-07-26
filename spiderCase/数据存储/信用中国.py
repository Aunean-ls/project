import csv
import json
import pandas as pd
import requests
from lxml import etree

headers = {
    'Host': 'creditbj.jxj.beijing.gov.cn',
    'Connection': 'keep-alive',
    'Content-Length': '95',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
    'Content-Type': 'application/json',
    'Origin': 'http://creditbj.jxj.beijing.gov.cn',
    'Referer': 'http://creditbj.jxj.beijing.gov.cn/credit-portal/credit_service/focus/list',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
request_payload = {
    "listSql": "",
    "linesPerPage": 10,
    "currentPage": 1,
    "condition": {"keyWord": "", "sourcePlatform": ""}
}
data_list = []


def crawl(url):
    # 步骤二：发送 HTTP 请求
    # 步骤三：获取响应数据
    response = requests.post(url=url, data=json.dumps(request_payload), headers=headers).json()
    # 步骤四：解析数据
    for info in response['data']['list']:
        data = {
            'id': info['xdrGszc'],
            'company': info['xdrMc'],
            'person': info['frdb'],
            'collDeptName': info['collDeptName'],
            'updateTime': info['updateTime']
        }
        print(data)
        data_list.append(data)


# 步骤五：存储数据
def save_data():
    df = pd.DataFrame(data=data_list, columns=['id', 'company', 'person', 'collDeptName', 'updateTime'])
    df.to_csv("Chengxin.csv", encoding='utf-8')


if __name__ == '__main__':
    # 步骤一：确定url
    base_url = 'http://creditbj.jxj.beijing.gov.cn/credit-portal/api/publicity/record/JYYCML/0'
    crawl(base_url)
    save_data()

# http://creditbj.jxj.beijing.gov.cn/credit-portal/credit_service/focus/list
