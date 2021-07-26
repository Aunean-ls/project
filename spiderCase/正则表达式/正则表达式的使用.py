import re
import requests
import os

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'
}


def crawl(url):
    response = requests.get(url, headers).content.decode('utf-8')

    img_list = re.findall('<div class="thumb".*?<img src="(.*?)" alt.*?</div>', response, re.S)

    for img in img_list:
        img = 'http:' + img
        print(img)

        path = 'qiushi_img/'
        if not os.path.exists(path):
            os.makedirs(path)
        img_data = requests.get(url=img, headers=headers).content
        img_name = img.split('/')[-1]

        with open(path + img_name, 'wb') as f:
            f.write(img_data)


if __name__ == '__main__':
    urls = ['https://www.qiushibaike.com/imgrank/page/{}/'.format(i) for i in range(1, 6)]
    for url in urls:
        crawl(url)

# html_str = """
#     Python3 高级开发工程师 上海互教教育科技有限公司上海-浦东新区2万/月02-18满员
#     测试开发工程师（C++/python） 上海墨鹍数码科技有限公司上海-浦东新区2.5万/每月02-18未满员
#     Python3 开发工程师 上海德拓信息技术股份有限公司上海-徐汇区1.3万/每月02-18剩余11人
#     测试开发工程师（Python） 赫里普（上海）信息科技有限公司上海-浦东新区1.1万/每月02-18剩余5人
#     Python高级开发工程师 上海行动教育科技股份有限公司上海-闵行区2.8万/月02-18剩余255人
#     python开发工程师 上海优似腾软件开发有限公司上海-浦东新区2.5万/每月02-18满员
# """
# '使用正则表达式提取工资，比如2,2.5,1.3...'
#
# result = re.findall('[\d.]*万', html_str)
# print(result)
#
# '''
# 第二题：提取百度页面中所有a链接的文字
# 比如，使用正则表达式提取文字“新闻”。
# '''
# b = '''<a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a>'''
# url = 'https://www.baidu.com/'
# response = requests.get(url, headers).content.decode('utf-8')
# a_list = re.findall('<a.*?</a>+', response, re.S)
# for a in a_list:
#     print(a)
#     result = re.findall('[\u4e00-\u9fa5]+', a, re.S)
#     print(result)
