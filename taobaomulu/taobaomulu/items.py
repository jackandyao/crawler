# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class TaobaomuluItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mulu_level1 = Field()
    mulu_level2 = Field()
    mulu_level3 = Field()
    pass
