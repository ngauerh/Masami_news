# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    url = scrapy.Field()
    summary = scrapy.Field()  # 摘要
    source = scrapy.Field()   # 新闻来源
    category = scrapy.Field()   # 新闻类别
    news_time = scrapy.Field()   # 新闻时间
    details = scrapy.Field()   # 全文



