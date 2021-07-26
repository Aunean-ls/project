import requests
import csv
import time


headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)'
}
all_content = []
workName = input('请输入你要找的工作：')
page = 0


def crawl(href):
    time.sleep(1.5)
    response = requests.get(url=href, headers=headers).json()['engine_search_result']
    print(response)
    for page_data in response:
        data = {
            '岗位名称': page_data['job_name'],
            '工作地点': page_data['workarea_text'],
            '薪资': page_data['providesalary_text'],
            '公司名称': page_data['company_name'],
            '招聘详情': page_data['job_href'],
            '工作福利': page_data['jobwelf'],
            '公司类型': page_data['companytype_text']
        }
        # print(data)
        all_content.append(data)


def saveData():
    with open('../data/originalData.csv', 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['岗位名称', '工作地点', '薪资',  '公司名称', '招聘详情', '工作福利', '公司类型']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_content)

'https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?'
if __name__ == '__main__':
    urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?'.format(workName, i) for i in range(1, 2)]
    for url in urls:
        page += 1
        print('==========================正在爬取第%d页数据========================' % page)
        crawl(url)
    saveData()


