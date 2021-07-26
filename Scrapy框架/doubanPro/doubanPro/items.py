# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    age = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    film_length = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    type = scrapy.Field()
    to_star = scrapy.Field()
    score = scrapy.Field()
    img = scrapy.Field()
    summary = scrapy.Field()
    # image_url = scrapy.Field()
