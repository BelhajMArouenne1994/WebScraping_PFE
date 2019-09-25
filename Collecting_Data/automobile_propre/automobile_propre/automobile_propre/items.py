# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Review(scrapy.Item):
    ID = scrapy.Field()
    Text = scrapy.Field()
    Date = scrapy.Field()
    car = scrapy.Field()
    Country = scrapy.Field()
    Page_Type = scrapy.Field()
