# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position = scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    work_location = scrapy.Field()
    info = scrapy.Field()
    # experience = scrapy.Field()
    # education = scrapy.Field()
    # number_recruiters = scrapy.Field()
    # position_type = scrapy.Field()
    company_size = scrapy.Field()
    update_time = scrapy.Field()
    requirement = scrapy.Field()

