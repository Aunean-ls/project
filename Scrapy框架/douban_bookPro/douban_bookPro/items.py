# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ISBN = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    score = scrapy.Field()
    price = scrapy.Field()
    page = scrapy.Field()
    time = scrapy.Field()
    press = scrapy.Field()
    translator = scrapy.Field()
    binding = scrapy.Field()
    comments = scrapy.Field()
    link = scrapy.Field()
    img_url = scrapy.Field()
