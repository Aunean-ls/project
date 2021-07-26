import scrapy
from qianchengPro.items import QianchengproItem


class QianchengSpider(scrapy.Spider):
    name = 'qiancheng'
    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']
    workName = input('请输入你要找的工作：')
    page = 0

    def start_requests(self):
        urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?'.format(self.workName, i) for i
                in range(1, 2)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response, **kwargs):

        content = response.json()['engine_search_result']
        self.page += 1
        print('==========================正在爬取第%d页数据========================' % self.page)
        print(content)
        for page_data in content:
            item = QianchengproItem()
            item['jobName'] = page_data['job_name']
            item['workArea'] = page_data['workarea_text']
            item['salary'] = page_data['providesalary_text']
            item['companyName'] = page_data['company_name']
            item['welfare'] = page_data['jobwelf']
            item['companyType'] = page_data['companytype_text']
            item['degreeFrom'] = page_data['degreefrom']
            item['workYear'] = page_data['workyear']
            item['issueDate'] = page_data['issuedate']
            item['companySize'] = page_data['companysize_text']
            item['jobHref'] = page_data['job_href']

            # print(item)
            yield item
