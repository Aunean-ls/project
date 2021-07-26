# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urlencode
from imagePro.items import ImageproItem
import json


class ImageSpider(scrapy.Spider):
    name = 'image'

    # allowed_domains = ['www.templates.com']
    # start_urls = ['http://www.xxx.com/']

    def start_requests(self):
        base_url = 'http://image.so.com/j?'
        parm = {'q': input("请输入下载图片的类型：")}
        for page in range(1, self.settings.get('MAX_PAGE') + 1):
            parm['sn'] = page * 60
            parm['ps'] = page * 60
            url = base_url + urlencode(parm)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        json_data = json.loads(response.text)
        for elem in json_data['list']:
            item = ImageproItem()
            item['id'] = elem['id']
            item['title'] = elem['title']
            item['url'] = elem['thumb']
            item['width'] = elem['width']
            item['height'] = elem['height']
            print(item)
            yield item

