import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}

# 存放内容
content = []
word = input('请输入关键字：')
page = int(input('爬取多少页：'))


def crawl(url):
    for i in range(0, page):
        params = {
            'page': page,
            # 'region_1': '430100',
            'jtzw': word
        }
        # 步骤三：获取响应数据
        response = requests.post(url=url, params=params, headers=headers).content.decode('gbk')
        # 步骤四：数据解析
        soup = BeautifulSoup(response, 'lxml')
        # 职位名称
        titles = soup.select('ul.search_result > li.search_post > a')

        # 企业名称
        companys = soup.select('ul.search_result > li.search_company > a:nth-child(1)')

        # 工作地区
        places = soup.select('ul.search_result > li.search_region')

        # 时间
        times = soup.select('ul.search_result > li.search_date')

        # 薪资
        salarys = soup.select('ul.search_result > li.search_salary')

        for i in range(len(titles)):
            title = titles[i].attrs['title']
            company = companys[i].attrs['title']
            place = places[i].text
            time = times[i].text
            salary = salarys[i].text
            print(title, company, place, time, salary)

            # 步骤五：存储数据
            with open('job1001.txt', 'a', encoding='utf-8') as f:
                f.writelines([title + '\t', company + '\t', place + '\t', time + '\t' + salary + '\n'])
    print('第'+str(page+1)+'页数据写入完毕')


if __name__ == '__main__':
    # 步骤一：确定url
    url = 'http://www.job1001.com/SearchResult.php'
    crawl(url)
