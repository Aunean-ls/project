# -*- coding: utf-8 -*-
import scrapy
from baixingPro.items import BaixingproItem
import time

class BaixingSpider(scrapy.Spider):
    name = 'baixing'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://changsha.baixing.com/chengxuyuan/']

    def parse(self, response):
        li_list = response.xpath('//div[@class="main"]/div/ul/li')
        print(li_list)
        for li in li_list:
            salary = li.xpath('.//div/span[@class="salary"]/text()').extract_first()
            info = li.xpath('./div/div[@class="table-view-cap job-list"]/text()').extract()
            info = ''.join(info).strip()
            treatment = li.xpath('.//div[@class="wellfares-badges"]/label/text()').extract()
            treatment = '，'.join(treatment)
            item = BaixingproItem()
            item['salary'] = salary
            item['info'] = info
            item['treatment'] = treatment
            print(salary)
            yield item
        time.sleep(2)
        next_url = response.xpath("/html/body/section/div/section/ul/li[last()]/a[contains(text(),'下一页')]/@href").extract_first()
        print("网址：", next_url)
        next_url = 'https://changsha.baixing.com' + next_url
        yield scrapy.Request(next_url, callback=self.parse)
