# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WubaproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    company = scrapy.Field()
    education = scrapy.Field()
    experience = scrapy.Field()
    welfare = scrapy.Field()
    pass
