import scrapy
from biaoqingPro.items import BiaoqingproItem

class BiaoqingSpider(scrapy.Spider):
    name = 'biaoqing'
    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']

    def start_requests(self):
        urls = ['http://www.bbsnet.com/biaoqingbao/page/{}'.format(i) for i in range(1, 2)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        li_list = response.xpath('//ul[@id="post_container"]/li')
        for li in li_list:
            title = li.xpath('./div/a/@title').extract_first()
            url = li.xpath('./div/a/img/@src').extract_first()
            time = li.xpath('./div[4]/span/text()').extract_first()

            item = BiaoqingproItem()
            item['title'] = title
            item['url'] = url
            item['time'] = time
            # print(item)
            yield item



