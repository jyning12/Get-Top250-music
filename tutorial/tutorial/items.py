# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    song_name = scrapy.Field()
    singer_name = scrapy.Field()
    year = scrapy.Field()
    class_ = scrapy.Field()
    rating_nums = scrapy.Field()

