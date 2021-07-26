# -*- coding: utf-8 -*-
import scrapy
from wanguPro.items import WanguproItem


class WanguSpider(scrapy.Spider):
    name = 'wangu'
    # allowed_domains = ['www.xsbiquge.com/20_20331/']
    start_urls = ['http://www.xsbiquge.com/20_20331/']

    def parse(self, response):
        detail_urls = response.xpath('//div[@id="list"]/dl/dd/a/@href').extract()
        for detail_url in detail_urls:
            detail_url = 'https://www.xsbiquge.com' + detail_url
            print(detail_url)

            yield scrapy.Request(detail_url, callback=self.detail_parse)

    def detail_parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('\xa0\xa0\xa0\xa0', '').replace('&#039;', '')
        print(title)
        item = WanguproItem()
        item['title'] = title
        item['content'] = content
        yield item


