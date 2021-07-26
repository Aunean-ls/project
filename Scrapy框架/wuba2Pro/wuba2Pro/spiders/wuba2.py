# -*- coding: utf-8 -*-
import scrapy
from wuba2Pro.items import Wuba2ProItem


class Wuba2Spider(scrapy.Spider):
    name = 'wuba2'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://cs.58.com/job/pn10/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0019-e5b1-eb6a-7f92b6d280ad&ClickID=3']

    def parse(self, response):
        li_list = response.xpath('//ul[@id="list_con"]/li')
        for li in li_list:
            url = li.xpath('.//a/@href').extract_first()

            yield scrapy.Request(url, callback=self.detail_parse)

            next_url = response.xpath('/html/body/div[3]/div[4]/div[1]/div[2]/a[@class="next"]/@href').extract_first()
            if next_url:
                yield scrapy.Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        position = response.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/span[1]/text()').extract_first()
        pos_name = response.xpath('/html/body/div[3]/div[3]/div[1]/span/text()').extract_first()
        salary = response.xpath('/html/body/div[3]/div[3]/div[1]/div[2]/span[2]/text()').extract_first()
        company_name = response.xpath('/html/body/div[3]/div[4]/div[1]/div/div[1]/div/div/a/text() | '
                                      '/html/body/div[3]/div[4]/div[1]/div/div[1]/div[1]/a/text()').extract_first()
        number_recruiters = response.xpath('/html/body/div[3]/div[3]/div[1]/div[4]/span[1]/text()').extract_first()
        # apply_num = response.xpath('//*[@id="apply_num"]/text()').extract_first()
        # total_count = response.xpath('//*[@id="totalcount"]/text()').extract_first()
        des = response.xpath('/html/body/div[3]/div[3]/div[2]/div[1]/div[1]/div[1]/text()').extract()
        des = ''.join(des).strip()
        education = response.xpath('/html/body/div[3]/div[3]/div[1]/div[4]/span[2]/text()').extract_first()
        work_location = response.xpath('/html/body/div[3]/div[3]/div[1]/div[5]/span[2]/text()').extract_first()

        item = Wuba2ProItem()

        item['position'] = position
        item['pos_name'] = pos_name
        item['salary'] = salary
        item['company_name'] = company_name
        item['number_recruiters'] = number_recruiters
        # item['apply_num'] = apply_num
        # item['total_count'] = total_count
        item['des'] = des
        item['education'] = education
        item['work_location'] = work_location
        print(item)
        yield item


