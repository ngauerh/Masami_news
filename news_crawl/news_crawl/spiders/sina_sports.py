import scrapy
from utils.n_crawl import *
from utils.db_access import *

from news_crawl.items import NewsCrawlItem
import time

class DmozSpider(scrapy.Spider):
    name = "sina_sports"
    allowed_domains = ["https://sports.sina.com.cn/global/"]
    start_urls = [
        "https://sports.sina.com.cn/global/"
    ]

    def parse(self, response):
        try:
            for sel in response.xpath('//div[@class="blk2"]'):
                item = NewsCrawlItem()
                for i in range(len(sel.xpath('//div[@class="blk2"]/ul/li/a/text()').extract())):
                    item['title'] = sel.xpath('//div[@class="blk2"]/ul/li/a/text()').extract()[i]
                    item['url'] = sel.xpath('//div[@class="blk2"]/ul/li/a/@href').extract()[i]
                    if url_same:
                        item['details'] = sina(item['url']).lstrip('[').rstrip(']')
                        item['summary'] = sina_s(item['url'])
                        item['source'] = '新浪体育'
                        item['category'] = '足球'
                        item['news_time'] = time.time()
                        yield item
                    else:
                        continue
        except:
            print('error')
