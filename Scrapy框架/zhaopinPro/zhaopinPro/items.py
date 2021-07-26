# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    company_name = scrapy.Field()
    edu_level = scrapy.Field()
    job_name = scrapy.Field()
    salary = scrapy.Field()
    create_time = scrapy.Field()
    city_name = scrapy.Field()
    company_size = scrapy.Field()
    welfare = scrapy.Field()
    responsibility = scrapy.Field()
    place = scrapy.Field()
    workingExp = scrapy.Field()
