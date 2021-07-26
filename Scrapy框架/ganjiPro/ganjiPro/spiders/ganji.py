# -*- coding: utf-8 -*-
import scrapy
from ganjiPro.items import GanjiproItem


class GanjiSpider(scrapy.Spider):
    name = 'ganji'

    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://bj.ganji.com/gongsi/']
    def start_requests(self):
        urls = ['http://bj.ganji.com/gongsi/o{}/'.format(i) for i in range(1, 4)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        url_links = response.xpath('//div[@class="com-list-2"]//tr/td/a/@href').extract()
        for url_link in url_links:
            yield scrapy.Request(url_link, callback=self.detail_parse)
        next_url = response.xpath('//*[@id="wrapper"]/div[4]/div/ul/li[last()]/a/@href')
        # if next_url:
        #     next_url = 'http://bj.ganji.com' + next_url
        #     yield scrapy.Request(next_url, callback=self.parse)

    def detail_parse(self, response):
        item = GanjiproItem()
        company_name = response.xpath('//*[@id="wrapper"]/div[4]/div[1]/div[1]/ul/li[1]/span[2]/text()').extract_first()
        company_type = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[1]/ul/li[4]/span[2]/a/text()').extract_first()
        company_industry = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[1]/ul/li[3]/span[2]/a/text()').extract_first()
        company_size = response.xpath('//*[@id="wrapper"]/div[4]/div[1]/div[1]/ul/li[2]/span[2]/text()').extract_first()
        company_introduction = response.xpath('//*[@id="company_description"]/text()').extract()
        company_introduction = ''.join(company_introduction).strip().replace(' ', '').replace('\r\n', '')
        position = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[1]/a/text()').extract_first()
        salary = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[2]/text() | //*[@id="wrapper"]/div[4]/div[1]/div[4]/table/tbody/tr[2]/td[2]/text()').extract_first()
        level = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[3]/text() | //*[@id="wrapper"]/div[4]/div[1]/div[4]/table/tbody/tr[2]/td[3]/text()').extract_first()
        number_recruiters = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[4]/text() | //*[@id="wrapper"]/div[4]/div[1]/div[4]/table/tbody/tr[2]/td[4]/text()').extract_first()
        work_location = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[5]/text() | //*[@id="wrapper"]/div[4]/div[1]/div[4]/table/tbody/tr[2]/td[5]/text()').extract_first()
        update_time = response.xpath(
            '//*[@id="wrapper"]/div[4]/div[1]/div[3]/table/tbody/tr[2]/td[6]/text() | //*[@id="wrapper"]/div[4]/div[1]/div[4]/table/tbody/tr[2]/td[6]/text()').extract_first()

        item['company_name'] = company_name
        item['company_type'] = company_type
        item['company_industry'] = company_industry
        item['company_size'] = company_size
        item['company_introduction'] = company_introduction
        item['position'] = position
        item['salary'] = salary
        item['level'] = level
        item['number_recruiters'] = number_recruiters
        item['work_location'] = work_location
        item['update_time'] = update_time

        yield item
        print(item)
