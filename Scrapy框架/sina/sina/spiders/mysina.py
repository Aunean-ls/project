import scrapy

from ..items import SinaItem

# 导入CrawlSpider: 连续爬取网页
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


# 使用CrawlSpider
class MysinaSpider(CrawlSpider):
    name = 'mysina'
    # allowed_domains = ['sina.com.cn']
    start_urls = ['https://roll.news.sina.com.cn/news/gnxw/gdxw1/indwx_1.shtml']

    # 定义rules：提取链接的规则
    rules = [
        Rule(
            LinkExtractor(
                allow=('indwx_\d+'),  # 匹配哪些href的链接内存 支持正则
                restrict_xpaths=('//div[@class="pagebox"]',),
            ),
            callback='parse_item',
            follow=True
        )
    ]
    print(start_urls)

    def parse_item(self, response):
        print(12)
        print(response)
        news_list = response.xpath('//ul[@class="list_009"]/li')
        print(news_list)

        for news in news_list:
            # 新闻标题
            news_title = news.xpath('./a/text()').get()
            # 时间
            news_time = news.xpath('./span/text()').get()

            # print(news_title,news_time)
            item = SinaItem()
            item['newstitle'] = news_title
            item['newstime'] = news_time
            print(item)
            yield item  # 需要存数据就写

# class MysinaSpider(scrapy.Spider):
#     name = 'mysina'
#     allowed_domains = ['sina.com.cn']
#     start_urls = ['https://roll.news.sina.com.cn/news/gnxw/gdxw1/indwx_1.shtml']
#
#     def parse(self, response):
#
#         print('*'*100)
#         print(response.text)
#         print('*'*100)
#         #使用xpath
#         news_list = response.xpath('//ul[@class="list_009"]/li')
#         # print(news_list)
#
#         for news in news_list:
#             #新闻标题
#             news_title = news.xpath('./a/text()').get()
#             #时间
#             news_time = news.xpath('./span/text()').get()
#
#             # print(news_title,news_time)
#             item = SinaItem()
#             item['newstitle'] = news_title
#             item['newstime'] = news_time
#             yield item #需要存数据就写
# https://roll.news.sina.com.cn/news/gnxw/gdxw1/indwx_1.shtml

# =====================================================================
