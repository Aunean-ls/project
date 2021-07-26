# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CnCityproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    location_id = scrapy.Field()
    city_name = scrapy.Field()
    country_name = scrapy.Field()
    adm1 = scrapy.Field()
    adm2 = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    code = scrapy.Field()
