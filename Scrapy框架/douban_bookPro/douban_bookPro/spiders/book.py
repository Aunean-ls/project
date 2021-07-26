# -*- coding: utf-8 -*-
import scrapy
from douban_bookPro.items import DoubanBookproItem


class BookSpider(scrapy.Spider):
    name = 'book'

    def start_requests(self):
        urls = ['https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6?start={}&type=T'.format(i) for i in
                range(0, 20, 20)]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
            print(url)

    def parse(self, response):
        # print(response)
        detail_links = response.xpath('//ul[@class="subject-list"]/li')

        for li in detail_links:
            link = li.xpath('./div/a/@href').extract_first()
            img_url = li.xpath('./div/a/img/@src').extract_first()
            info = li.xpath('./div[2]/div[1]/text()').extract_first().strip()
            info = str(info).split('/')
            author = info[0].rstrip()
            translator = info[1].strip()
            press = info[2].strip()
            price = info[4].strip()
            req = scrapy.Request(url=link, callback=self.detail_parse)

            req.meta['link'] = link
            req.meta['img_url'] = img_url
            req.meta['author'] = author
            req.meta['translator'] = translator
            req.meta['press'] = press
            req.meta['price'] = price
            yield req

    def detail_parse(self, response):
        title = response.xpath('//h1/span/text()').extract_first()
        time = response.xpath('//*[@id="info"]/text()[last()-11]').extract_first().strip()
        if time is '':
            time = response.xpath('//*[@id="info"]/text()[last()-9]').extract_first().strip()
        page = response.xpath('//*[@id="info"]/text()[last()-9]').extract_first().strip()
        if len(page.split('-')) > 1:
            page = response.xpath('//*[@id="info"]/text()[last()-7]').extract_first().strip()
        binding = response.xpath('//*[@id="info"]/text()[last()-5]').extract_first().strip()
        ISBN = response.xpath('//*[@id="info"]/text()[last()-1]').extract_first().strip()
        score = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first().strip()
        comments = response.xpath('//*[@id="interest_sectl"]/div/div[2]/div/div[2]/span/a/span/text()').extract_first()

        item = DoubanBookproItem()

        item['ISBN'] = ISBN
        item['title'] = title
        item['author'] = response.meta['author']
        item['score'] = score
        item['price'] = response.meta['price']
        item['page'] = page
        item['time'] = time
        item['press'] = response.meta['press']
        item['translator'] = response.meta['translator']
        item['binding'] = binding
        item['comments'] = comments
        item['link'] = response.meta['link']
        item['img_url'] = response.meta['img_url']

        yield item
        print(item)
