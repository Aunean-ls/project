# -*- coding: utf-8 -*-
import scrapy
from maoyanPro.items import MaoyanproItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    # allowed_domains = ['https://maoyan.com/board/4?offset=0']
    start_urls = ['https://maoyan.com/board/4?offset=0']

    def parse(self, response):
        dd_list = response.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
        # print(dd_list)
        for dd in dd_list:
            item = MaoyanproItem()
            item["title"] = dd.xpath('./a/@title').extract_first()
            item["actor"] = (''.join(dd.xpath('./div//p[@class="star"]/text()').extract()).strip())[3:]
            item["time"] = dd.xpath('./div//p[@class="releasetime"]/text()').extract_first()[5:]
            item["score"] = ''.join(dd.css('p.score i::text').extract())
            print(item)
            yield item

        next_url = response.xpath('//*[@id="app"]//div[2]/ul/li[last()]/a/@href').extract_first()
        if next_url != 'javascript:void(0);':
            next_url = 'https://maoyan.com/board/4' + next_url

            yield scrapy.Request(next_url, callback=self.parse)

#
# import scrapy
# from maoyan.items import MaoyanItem
#
#
# class MoviesSpider(scrapy.Spider):
#     name = 'movies'
#     allowed_domains = ['127.0.0.1']
#     offset = 0
#     url = "http://127.0.0.1:8080/board/4?offset="
#     # ********** Begin **********#
#     # 1.对url进行定制，为翻页做准备
#     start_url = ["http://127.0.0.1:8080/board/4?offset={}".format(offset)]
#
#     # 2.定义爬虫函数parse()
#     def parse(self, response):
#         movies = response.xpath("//div[ @class ='board-itemcontent']")
#         for each in movies:
#             item = MaoyanItem()
#             # 电影名
#             name = each.xpath(".//div/p/a/text()").extract()[0]  # 注意extract()函数返回的是一个list列表，这里我们只需要单个元素，所以加[0]
#             # 主演明星                                              #把它取出来，extract()[0]的作用同extract_first()
#             starts = each.xpath(".//div[1]/p/text()").extract()[0]
#             # 上映时间
#             releasetime = each.xpath(".//div[1]/p[3]/text()").extract()[0]
#             score1 = each.xpath(".//div[2]/p/i[1]/text()").extract()[0]
#             score2 = each.xpath(".//div[2]/p/i[2]/text()").extract()[0]
#
#             # 评分
#             score = score1 + score2
#             item['name'] = name
#             item['starts'] = starts
#             item['releasetime'] = releasetime
#             item['score'] = score
#             yield item
#
#     # 3.在函数的最后offset自加10，然后重新发出请求实现翻页功能
#         if self.offset < 100:
#             self.offset += 10
#             yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
