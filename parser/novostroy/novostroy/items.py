# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
 
class NovostroyItem(scrapy.Item):
    name = scrapy.Field()
    district = scrapy.Field()
    image = scrapy.Field()
    room_types = scrapy.Field()
    studio = scrapy.Field()
    one_room = scrapy.Field()
    two_room = scrapy.Field()
    three_room = scrapy.Field()
    four_room = scrapy.Field()
    multiroom = scrapy.Field()
