# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Wuba2ProItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()
    pos_name = scrapy.Field()
    salary = scrapy.Field()
    company_name = scrapy.Field()
    number_recruiters = scrapy.Field()
    apply_num = scrapy.Field()
    total_count = scrapy.Field()
    des = scrapy.Field()
    education = scrapy.Field()
    work_location = scrapy.Field()

