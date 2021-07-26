# -*- coding: utf-8 -*-
import scrapy
from dianpingPro.items import DianpingproItem


class DianpinSpider(scrapy.Spider):
    name = 'dianpin'

    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        # cookies = {'lgtoken': '04d5b4b63-f50f-4701-873f-cb686fdea05e',
        #            'thirdtoken': '542f53b3-3259-405c-bc2a-29a6fe9024e7',
        #            'dplet': '45dcd95b2c7e1cc2c028bb808f1f3b6b',
        #            'dper': '9e2ec7f7ae0a361117e405578541cedcde5146b0e18890060195789c601e0564199e6e85e1d1d060388dae0bebea14b3afb49b4dd355678ffd467dbff8fd9219',
        #            'll': '7fd06e815b796be3df069dec7836c3df',
        #            'ua': 'dpuser_8517583926;',
        #            'ctu': '3877de628f129d466680c64a83ca271add57718a0310c1a76b4f2150a544e11d',
        #            'fspop': 'test',
        #            'cy': '344',
        #            'cye': 'changsha',
        #            '_lxsdk_cuid': '17655e01e9ba-0f3973c7e1d8fa-4c3f2779-144000-17655e01e9cc8',
        #            '_lxsdk_s': '17655e01e9d-6d4-5ac-1d0%7C%7C57',
        #            '_lxsdk': '17655e01e9ba-0f3973c7e1d8fa-4c3f2779-144000-17655e01e9cc8',
        #            '_hc.v': 'dcba044f-796d-7250-b9c7-2c1ac14c469c.1607758521',
        #            'JSESSIONID': 'D243D2DCCA22BE56996069C93C83A70D'}

        urls = ['http://t.dianping.com/list/xian-category_15?pageIndex={}'.format(i) for i in range(1, 50)]

        for url in urls:
            print(url)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//*[@id="body"]/div[2]/div[4]/div[1]/ul/li')
        print(li_list)
        for li in li_list:
            shop_name = li.xpath('.//h3/text()').extract_first()
            original_price = li.xpath('./div/span[1]/span[2]/del/text()').extract_first()
            discount_price = li.xpath('./div/span[1]/span[1]/em/text()').extract_first()
            sale_total = li.xpath('./div/span[2]/text()').extract_first()
            sale_total = str(sale_total).strip()
            icon = li.xpath('./div/div/ul/li[2]/text()').extract_first()
            detail_url = li.xpath('./div/a[1]/@href').extract_first()
            detail_url = 'http://t.dianping.com' + detail_url

            item = DianpingproItem()

            item['shop_name'] = shop_name
            item['original_price'] = original_price
            item['discount_price'] = discount_price
            item['sale_total'] = sale_total
            item['icon'] = icon
            item['detail_url'] = detail_url
            print(item)
            yield item
