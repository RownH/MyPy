# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class PropertiesItem(scrapy.Item):
    title=Field()
    price=Field()
    description=Field()
    address=Field()
    image_urls=Field()
    images=Field()
    location=Field()
    url=Field()
    project=Field()
    spider=Field()
    server=Field()
    date=Field()