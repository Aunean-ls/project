# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GanjiproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    company_type = scrapy.Field()
    company_industry = scrapy.Field()
    company_size = scrapy.Field()
    company_introduction = scrapy.Field()
    position = scrapy.Field()
    salary = scrapy.Field()
    level = scrapy.Field()
    number_recruiters = scrapy.Field()
    work_location = scrapy.Field()
    update_time = scrapy.Field()
    pass
