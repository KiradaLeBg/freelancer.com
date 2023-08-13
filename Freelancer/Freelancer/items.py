# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    link = scrapy.Field()
    job_title = scrapy.Field()
    location = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
    proposal = scrapy.Field()