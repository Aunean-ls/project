# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DianpingproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shop_name = scrapy.Field()
    original_price = scrapy.Field()
    discount_price = scrapy.Field()
    sale_total = scrapy.Field()
    icon = scrapy.Field()
    detail_url = scrapy.Field()
