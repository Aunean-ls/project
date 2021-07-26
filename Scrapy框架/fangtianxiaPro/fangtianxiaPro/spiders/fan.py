# -*- coding: utf-8 -*-
import scrapy
from fangtianxiaPro.items import FangtianxiaproItem


class FanSpider(scrapy.Spider):
    name = 'fan'
    # allowed_domains = ['www.templates.com']
    # start_urls = ['https://sh.newhouse.fang.com/house/s/a77-b91/']

    def start_requests(self):
        url_list = ['https://sh.newhouse.fang.com/house/s/a77-b9{}/'.format(i) for i in range(1, 31)]
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        div_list = response.xpath('//div[@class="nhouse_list"]/div/ul/li')
        for div in div_list:
            title = div.xpath('.//div[@class="nlcd_name"]/a/text()').extract_first()
            title = str(title).strip()
            address = div.xpath('.//div[@class="address"]/a/@title').extract_first()
            price = div.xpath('.//div[@class="nhouse_price"]/span/text()').extract_first()
            tel = div.xpath('.//div[@class="tel"]/p/text()').extract_first()

            item = FangtianxiaproItem()
            item['title'] = title
            item['address'] = address
            item['price'] = price
            item['tel'] = tel
            yield item

        # next_url = response.xpath('//ul/li[@class="fr"]/a[@class="next"]/@href').extract_first()
        # next_url = 'https://sh.newhouse.fang.com' + next_url
        # yield scrapy.Request(next_url, callback=self.parse)
        # url = response.xpath("//a[contains(text(),'下一页')]/@href").extract()
