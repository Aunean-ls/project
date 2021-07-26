# -*- coding: utf-8 -*-
import scrapy
from wubaPro.items import WubaproItem

class WubaSpider(scrapy.Spider):
    name = 'wuba'
    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        urls = ['https://search.chinahr.com/bj/job/pn{}/?key=Java%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88'.format(i) for i in range(1, 10)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data_details = response.xpath('//div[@class="job-list-box"]/div[1]')
        for data_detail in data_details:
            detail = data_detail.xpath('./@data-detail').extract_first()
            # print(detail)
            yield scrapy.Request(detail, callback=self.detail_parse)

    def detail_parse(self, response):
        position = response.xpath('//h1/text()').extract_first()
        company_name = response.xpath('/html/body/div[4]/div/div[2]/div/span[1]/text()').extract_first()
        salary = response.xpath('/html/body/div[4]/div/div[1]/div[1]/span[1]/text()').extract_first()
        work_location = response.xpath('/html/body/div[4]/div/div[1]/div[3]/span/text()').extract_first()
        work_location = str(work_location).strip()

        info = response.xpath('/html/body/div[4]/div/div[1]/div[1]/span[2]/text()').extract_first()
        # info = str(info).split('|')
        # experience = str(info[1]).strip()
        # education = str(info[2]).strip()
        # number_recruiters = str(info[3]).replace('招', '').strip()
        # position_type = str(info[4]).strip()

        company_size = response.xpath('/html/body/div[4]/div/div[2]/div/span[2]/text()').extract_first()
        # company_size = str(company_size).split('|')[1]

        update_time = response.xpath('/html/body/div[4]/div/div[1]/div[4]/span/text()').extract_first()
        requirement = response.xpath('/html/body/div[5]/div[1]/div[1]/div[1]/div/text()').extract()
        requirement = ''.join(requirement).strip()

        item = WubaproItem()

        item['position'] = position
        item['company_name'] = company_name
        item['salary'] = salary
        item['work_location'] = work_location
        item['info'] = info
        # item['experience'] = experience
        # item['education'] = education
        # item['number_recruiters'] = number_recruiters
        # item['position_type'] = position_type
        item['company_size'] = company_size
        item['update_time'] = update_time
        item['requirement'] = requirement
        print(item)
        yield item


