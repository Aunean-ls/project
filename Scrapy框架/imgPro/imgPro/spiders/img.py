# -*- coding: utf-8 -*-
import scrapy

from imgPro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'

    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']
    def start_requests(self):
        urls = ['http://pic.netbian.com/4kdongman/index_{}.html'.format(i) for i in range(2, 3)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')
        for li in li_list:
            detail_url = li.xpath('./a/@href').extract_first()
            detail_url = 'http://pic.netbian.com' + detail_url
            yield scrapy.Request(url=detail_url, callback=self.detail_parse)

    def detail_parse(self, response):

        img_url = response.xpath('//div[@class="photo-pic"]/a/img/@src').extract_first()
        img_url = 'http://pic.netbian.com' + img_url
        img_name = response.xpath('//div[@class="photo-pic"]/a/img/@title').extract_first() + '.jpg'
        category = response.xpath('//div[@class="infor"]/p[1]//a/text()').extract_first()
        size = response.xpath('//div[@class="infor"]/p[2]/span/text()').extract_first()
        volume = response.xpath('//div[@class="infor"]/p[3]/span/text()').extract_first()
        time = response.xpath('//div[@class="infor"]/p[4]/span/text()').extract_first()
        item = ImgproItem()
        item['img_url'] = img_url
        item['img_name'] = img_name
        print(img_url)
        yield item
