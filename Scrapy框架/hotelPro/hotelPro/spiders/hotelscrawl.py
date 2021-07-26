# -*- coding: utf-8 -*-
import scrapy
import re
import json
from hotelPro.items import HotelproItem


class HotelscrawlSpider(scrapy.Spider):
    name = 'hotelscrawl'

    # allowed_domains = ['www.xx.com']
    # start_urls = ['http://www.xx.com/']
    def start_requests(self):
        url = 'http://172.16.10:8080/hotelManagerment/resources/is/kuCity.js'
        headers = {
            'Content-Type': 'application/x-www.form-urlencoded: charset=UTF-8'
        }
        yield scrapy.FormRequest(url=url, headers=headers, callback=self.get_city)

    def get_city(self, response):
        response = response.text
        response_first = re.findall('\[.*?\]', response, re.S)
        all_cities = re.findall('[\u4e00-\u9fa5]', response_first[0])

        url = 'http://172.16.10.10:8080/hotelManagement/getHotels.do'
        headers = {
            'Content-Type': 'application/x-www.form-urlencoded: charset=UTF-8'
        }
        for city in all_cities:
            data = {
                'city': city,
                'busDis': '',
                'star': '',
                'isTn': 2,
                'page': 1
            }
            yield scrapy.FormRequest(url=url, headers=headers, formdata=data, callback=self.get_page,
                                     meta={'city': city}, dont_filter=True)

    def get_page(self, response):
        total_page_num = json.loads(response.text)['totalPageNum']
        city = response.meta['city']
        url = 'http://172.16.10.10:8080/hotelManagement/getHotels.do'
        headers = {
            'Content-Type': 'application/x-www.form-urlencoded: charset=UTF-8'
        }
        for page in range(1, total_page_num + 1):
            data2 = {
                'city': city,
                'busDis': '',
                'star': '',
                'isTn': 2,
                'page': page
            }
            yield scrapy.FormRequest(url=url, headers=headers, formdata=data2, meta={'city': city, 'page': page})

    def get_hotel_id(self, response):
        hotel_id_list = json.loads(response.text)['hotels']

        url = 'http://172.16.10.10:8080/hotelManagement/hotelInfo.do'
        headers = {
            'Content-Type': 'application/x-www.form-urlencoded: charset=UTF-8'
        }
        for hotels_dict in hotel_id_list:
            hotel_id = hotels_dict.get('id')
            price = hotels_dict.get('price')
            data_id = {
                'id': hotel_id
            }
            yield scrapy.FormRequest(url=url, headers=headers, formdata=data_id, callback=self.parse,
                                     meta={'price': price}, dont_filter=True)

    def parse(self, response):
        item = HotelproItem()
        hotel_dict = json.loads(response.text)[0]
        hotel = {}
        detail = {}

        detail['SEQ'] = hotel_dict.get('seq')
        detail['国家'] = hotel_dict.get('country')
        detail['省份'] = hotel_dict.get('province')
        detail['城市'] = hotel_dict.get('city')
        detail['最低房间价格'] = response.meta['price']
        hotel['name'] = hotel_dict.get('hotel_name')
        hotel['detail'] = detail
        item['result'] = hotel
        yield item
