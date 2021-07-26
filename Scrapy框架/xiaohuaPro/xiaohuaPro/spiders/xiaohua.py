# -*- coding: utf-8 -*-
import scrapy
from xiaohuaPro.items import XiaohuaproItem


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'

    # allowed_domains = ['www.templates.cmo']
    # start_urls = ['http://www.xxx.cmo/']
    def start_requests(self):
        'http://joke.rain8.com/duanxin/list_7_1.html'
        # urls = ['http://joke.rain8.com/shunkouliu/list_34_{}.html'.format(i) for i in range(1, 21)]
        # for url in urls:
        #     yield scrapy.Request(url, callback=self.parse)
        urls2 = ['http://joke.rain8.com/duanxin/list_7_{}.html'.format(i) for i in range(1, 21)]
        for url in urls2:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//ul[@class="e2"]/li')
        for li in li_list:
            href = li.xpath('./a[1]/@href').extract_first()
            yield scrapy.Request(url=href, callback=self.detail_parse)

    def detail_parse(self, response):
        title = response.xpath('//h2/text()').extract_first()
        # time = response.xpath('//div[@class="info"]/text()[2]').extract_first().replace(' \r\n', '')
        # click_num = response.xpath('//div[@class="info"]/text()[4]').extract_first()
        content = response.xpath(
            '//div[@class="content"]//td/text() | //div[@class="content"]//td/div/text() | //div[@class="content"]//td/p/text()').extract()
        content = ''.join(content).strip().replace('\r\n', '').replace('\t', '').replace('\xa0', '').replace(
            '\u3000\u3000', '')

        item = XiaohuaproItem()
        item['title'] = title
        # item['time'] = time
        item['content'] = content
        yield item
        print(item)
