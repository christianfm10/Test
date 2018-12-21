# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TestSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    sneaker_price = scrapy.Field()
    sneaker_image = scrapy.Field()
    sneaker_url = scrapy.Field()
    sneaker_name = scrapy.Field()