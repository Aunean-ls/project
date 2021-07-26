import scrapy
from imagePro.items import ImageproItem
from urllib.parse import urlencode
import json


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://image.so.com/']
    # start_urls = ['http://pic.netbian.com/']

    headers = {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'
    }

    # def start_requests(self):
    #     urls = ['http://pic.netbian.com/4kdongman/index_{}.html'.format(i) for i in range(4, 5)]
    #     for url in urls:
    #         yield scrapy.Request(url, callback=self.parse)
    #
    # def parse(self, response):
    #     li_list = response.xpath('//ul[@class="clearfix"]/li')
    #     for li in li_list:
    #         detail_url = li.xpath('./a/@href').extract_first()
    #         detail_url = 'http://pic.netbian.com' + detail_url
    #         # print(detail_url)
    #         yield scrapy.Request(url=detail_url, headers=self.headers, callback=self.detail_parse)
    #
    # def detail_parse(self, response):
    #
    #     img_url = response.xpath('//div[@class="photo-pic"]/a/img/@src').extract_first()
    #     img_url = 'http://pic.netbian.com' + img_url
    #     # img_name = response.xpath('//div[@class="photo-pic"]/a/img/@title').extract_first() + '.jpg'
    #     # category = response.xpath('//div[@class="infor"]/p[1]//a/text()').extract_first()
    #     # size = response.xpath('//div[@class="infor"]/p[2]/span/text()').extract_first()
    #     # volume = response.xpath('//div[@class="infor"]/p[3]/span/text()').extract_first()
    #     # time = response.xpath('//div[@class="infor"]/p[4]/span/text()').extract_first()
    #     item = ImageproItem()
    #     item['url'] = img_url
    #     # print(item)
    #     # item['img_name'] = img_name
    #     # print(img_url)
    #     yield item

    def start_requests(self):
        base_url = 'http://image.so.com/j?'
        parm = {'q': input('请输入下载图片的类型：')}
        for page in range(1, self.settings.get('MAX_PAGE')+1):
            # parm['sn'] = 60 + 11 * page
            parm['ps'] = 188 + 60 * page
            parm['pc'] = 60
            url = base_url + urlencode(parm)  # 防止中文乱码
            yield scrapy.Request(url=url, headers=self.headers, callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.text)
        print(len(json_data['list']))
        for elem in json_data['list']:

            item = ImageproItem()
            item['id'] = elem['id']
            item['title'] = elem['title'].replace('<em>', '').replace('</em>', '')
            item['url'] = elem['thumb']
            item['width'] = elem['width']
            item['height'] = elem['height']
            item['imgsize'] = elem['imgsize']
            # print(item)
            yield item
