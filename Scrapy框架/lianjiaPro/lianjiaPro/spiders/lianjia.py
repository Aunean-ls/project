# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from lianjiaPro.items import LianjiaproItem


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    # allowed_domains = ['lianjia.com']
    start_urls = ['https://cs.lianjia.com/zufang/rs%E7%8F%A0%E6%B1%9F%E8%8A%B1%E5%9F%8E']

    # 第一个/默认的对应函数叫做parse
    def parse(self, response):
        # with open('lianjia.html', 'wb') as f:
        #     # 使用 body 来获取二进制的返回值信息
        #     f.write(response.body)

        # 通过XPATH获取具体的内容
        hrefs = response.xpath('//div[@class="content__list--item"]/a/@href').extract()
        # print(hrefs)
        # 循环访问每个详情页的信息
        for href in hrefs:
            href = parse.urljoin(response.url, href)
            req = scrapy.Request(url=href, callback=self.detail_parse)
            yield req

    def detail_parse(self, response):
        title = response.xpath('//p[@class="content__title"]/text()').extract_first()
        repair_time = response.xpath('//div[@class="content__subtitle"]/text()').extract_first().strip()[7:]
        price = response.xpath('//div[@class="content__aside--title"]/span/text()').extract_first()
        area = response.xpath('//div[@class="content__article__info"]/ul/li[2]/text()').extract_first()
        print(price)
        item = LianjiaproItem()
        item['title'] = title
        item['repair_time'] = repair_time
        item['price'] = price
        item['area'] = area
        yield item

