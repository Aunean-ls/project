import scrapy
from mongoingPro.items import MongoingproItem


class MongoingSpider(scrapy.Spider):
    name = 'mongoing'
    # allowed_domains = ['www.templates.com']
    start_urls = ['https://mongoing.com/zhangyaogxing']

    def parse(self, response):
        detail_urls = response.xpath('//div[@class="content"]/article/header//a/@href').extract()
        for detail_url in detail_urls:
            yield scrapy.Request(detail_url, callback=self.detail_parse)

    def detail_parse(self, response):
        title = response.xpath('//h1/a/text()').extract_first()
        time = response.xpath('//div[@class="article-meta"]/span[1]/text()').extract_first()
        content = response.xpath('//article[@class="article-content"]//text()').extract()
        content = ''.join(content).replace('\xa0\n', '').replace('\n', '').strip()
        item = MongoingproItem()
        item['title'] = title
        item['time'] = time
        item['content'] = content
        print(item)
        yield item
