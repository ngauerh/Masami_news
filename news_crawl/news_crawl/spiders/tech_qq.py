import scrapy
from news_crawl.items import NewsCrawlItem
from utils.n_crawl import *
from utils.db_access import *
import time


class TechSpider(scrapy.Spider):
    name = "tech_qq"
    allowed_domains = ["tech.163.com"]
    start_urls = ["http://tech.163.com/"]

    def parse(self, response):
        # sites = response.xpath('//div[@class="end-text"]/p')
        # content = []
        # for site in sites:
        #     content.append(''.join(site.xpath('text()').extract()))
        item = NewsCrawlItem()
        # item['article'] = response.url
        # item['desc'] = ''.join(content)
        # items.append(item)
        item['title'] = 1
        item['url'] = 2
        item['summary'] = 3
        item['source'] = 4
        item['category'] = 5
        item['news_time'] = 6
        item['details'] = 7
        print(item)
        yield item
