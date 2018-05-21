import scrapy
from news_crawl.items import NewsCrawlItem
from utils.n_crawl import *
from utils.db_access import *
import time


class Tech163Spider(scrapy.Spider):
    name = "tech_163"
    allowed_domains = ["tech.163.com/it/"]
    start_urls = ["http://tech.163.com/it/"]

    def parse(self, response):
        try:
            for sel in response.xpath('//div[@class="left w620"]/ul/li'):
                for i in range(len(sel.xpath('//div[@class="left w620"]/ul/li/div[@class="titleBar clearfix"]/h3/a/text()'))):
                    print(sel)
                    item = NewsCrawlItem()
                    item['title'] = sel.xpath('//div[@class="left w620"]/ul/li/div[@class="titleBar clearfix"]/h3/a/text()').extract()[i]
                    item['url'] = sel.xpath('//div[@class="left w620"]/ul/li/div[@class="titleBar clearfix"]/h3/a/@href').extract()[i]
                    item['details'] = tech163(item['url']).lstrip('[').rstrip(']')
                    item['summary'] = sel.xpath('//div[@class="left w620"]/ul/li/div[@class="clearfix"]').extract()[i]
                    item['source'] = '网易科技'
                    item['category'] = '科技'
                    item['news_time'] = time.time()
                    yield item
                break
            # else:
            #     continue
        except:
            print('error')

