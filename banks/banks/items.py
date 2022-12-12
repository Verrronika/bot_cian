# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BanksItem(scrapy.Item):
    # define the fields for your item here like:
    sum = scrapy.Field()
    term = scrapy.Field()
    name = scrapy.Field()
    pecentage = scrapy.Field()
    image = scrapy.Field()
    month = scrapy.Field()
    pass
