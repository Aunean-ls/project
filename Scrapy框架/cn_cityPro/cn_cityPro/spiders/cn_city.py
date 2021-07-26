# -*- coding: utf-8 -*-
import scrapy
from cn_cityPro.items import CnCityproItem


class CnCitySpider(scrapy.Spider):
    name = 'cn_city'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://github.com/qwd/LocationList/blob/master/China-City-List-latest.csv']

    def parse(self, response):
        tr_list = response.xpath('//div[@class="markdown-body"]//tr[position()>1]')
        for tr in tr_list:
            location_id = tr.xpath('./td[2]/text()').extract_first()
            city_name = tr.xpath('./td[4]/text()').extract_first()
            country_name = tr.xpath('./td[7]/text()').extract_first()
            adm1 = tr.xpath('./td[9]/text()').extract_first()
            adm2 = tr.xpath('./td[11]/text()').extract_first()
            latitude = tr.xpath('./td[12]/text()').extract_first()
            longitude = tr.xpath('./td[13]/text()').extract_first()
            code = tr.xpath('./td[14]/text()').extract_first()

            item = CnCityproItem()
            item['location_id'] = location_id
            item['city_name'] = city_name
            item['country_name'] = country_name
            item['adm1'] = adm1
            item['adm2'] = adm2
            item['latitude'] = latitude
            item['longitude'] = longitude
            item['code'] = code
            yield item
            print(item)  # 3240
