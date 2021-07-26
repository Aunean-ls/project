# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class QianchengproItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    workArea = scrapy.Field()
    salary = scrapy.Field()
    companyName = scrapy.Field()
    welfare = scrapy.Field()
    companyType = scrapy.Field()
    degreeFrom = scrapy.Field()
    workYear = scrapy.Field()
    issueDate = scrapy.Field()
    companySize = scrapy.Field()
    jobHref = scrapy.Field()

