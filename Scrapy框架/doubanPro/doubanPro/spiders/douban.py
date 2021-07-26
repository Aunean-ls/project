# -*- coding: utf-8 -*-
import scrapy
import json
from doubanPro.items import DoubanproItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'

    # allowed_domains = ['douban.com']
    # start_urls = ['http://douban.com/']
    # 去除start_urls之后，我们可以使用一个函数来替代它
    def start_requests(self):

        # base_url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}'
        base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20'
        for i in range(1, 2):
            url = base_url.format(i * 20)
            print(url)
            req = scrapy.Request(url=url, callback=self.parse)
            # req.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
            yield req

    def parse(self, response):
        print(response)
        json_str = response.body.decode('utf-8')
        print(json_str)
        res_dict = json.loads(json_str)
        # print(res_dict)
        for item in res_dict['subjects']:
            url = item['url']
            print(url)
            yield scrapy.Request(url=url, callback=self.parse_detail)

    def parse_detail(self, response):
        # scrapy shell https://movie.douban.com/subject/26981368/
        title = response.xpath('//h1/span[1]/text()').extract_first()
        age = response.xpath('//*[@id="info"]/span[11]/text()').extract_first()[:10]
        director = response.xpath('//div[@id="info"]/span[1]/span/a/text()').extract_first()
        screenwriter = '/'.join(response.xpath('//div[@id="info"]/span[2]/span/a/text()').extract())
        film_length = response.xpath('//*[@id="info"]/span[13]/text()').extract_first()[:-2]
        country = response.selector.re('制片国家/地区:</span>(.*?)<br>')[0].strip()
        language = response.selector.re('语言:</span>(.*?)<br>')[0].strip()
        type = '/'.join(response.selector.re('<span property="v:genre">(.*?)</span>'))
        to_star = '/'.join(response.selector.re('rel="v:starring">(.*?)</a>')[:3])
        score = response.selector.re('property="v:average">(.*?)</strong>')[0]
        img = response.xpath('//div[@id="mainpic"]/a/img/@src').extract_first()
        summary = ''.join(response.xpath('//span[@property="v:summary"]/text()').extract()).strip().replace(' ', '')
        print(title, age, director, score, type)
        # 按住Alt键
        item = DoubanproItem()
        item['title'] = title
        item['age'] = age
        item['director'] = director
        item['screenwriter'] = screenwriter
        item['film_length'] = film_length
        item['country'] = country
        item['language'] = language
        item['type'] = type
        item['to_star'] = to_star
        item['score'] = score
        item['img'] = img
        item['summary'] = summary

        # 下载图片
        # item['image_url'] = [img]
        yield item
