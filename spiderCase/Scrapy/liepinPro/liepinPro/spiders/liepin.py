import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from liepinPro.items import LiepinproItem


class LiepinSpider(CrawlSpider):
    name = 'liepin'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://www.liepin.com/zhaopin/?&key=python&curPage=0']

    # 定义超链接的提取规则
    page_link = LinkExtractor(allow=('&curPage=\d+'))
    # 定义爬取数据的规则
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = LiepinproItem()
        li_list = response.xpath('//ul[@class="sojob-list"]/li')
        for li in li_list:
            name = li.xpath('./div//h3/a/text()').extract_first().strip()
            print(name)
            company = li.xpath('./div/div[2]/p/a/text()').extract_first()
            info = li.xpath('./div/div[1]/p/@title').extract_first()
            time = li.xpath('./div/div[1]/p[2]/time/@title').extract_first()

            item['name'] = name
            item['company'] = company
            item['info'] = info
            item['time'] = time
            print(item)
            yield item
