import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wubaPro.items import WubaproItem


class WubaSpider(CrawlSpider):
    name = 'wuba'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://cs.58.com/tech/pn2/?param7503=1&from=yjz2_zhaopin']

    # 定义超链接的提取规则
    page_link = LinkExtractor(allow=('pn\d+'))
    # 定义爬取数据的规则
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_list = response.xpath('//ul[@id="list_con"]/li')
        for li in li_list:
            item = WubaproItem()
            # 岗位名
            name = li.xpath('./div[2]/p/span[1]/text()').extract_first()
            # 工资
            salary = li.xpath('./div[1]/p/text()').extract_first()
            # 公司名
            company = li.xpath('./div[2]/div/a/@title').extract_first()
            # 学历
            education = li.xpath('./div[2]/p/span[2]/text()').extract_first()
            # 工作经验
            experience = li.xpath('./div[2]/p/span[3]/text()').extract_first()
            # 福利
            welfare = li.xpath('./div[1]/div[2]/span/text()').extract()
            welfare = '_'.join(welfare)

            item['name'] = name
            item['salary'] = salary
            item['company'] = company
            item['education'] = education
            item['experience'] = experience
            item['welfare'] = welfare
            print(item)
            yield item




