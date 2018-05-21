# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from news_crawl.settings import DB
import pymysql


class NewsCrawlPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(DB['host'], DB['usr'], DB['password'], DB['db_name'], charset='utf8')
        self.cursor = self.conn.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()


class NewsMysqlPipeline(MysqlPipeline):
    def process_item(self, item,spider):
        sql = 'insert into n_news(title,url,summary,source,category,news_time,details) ' \
              'VALUES(%s,%s,%s,%s,%s,%s,%s) on duplicate key update title=values(title),summary=VALUES(summary),details=VALUES(details)'
        try:
            self.cursor.execute(sql, (item['title'], item['url'], item['summary'], item['source'], item['category'], item['news_time'], item['details']))
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            print('执行语句失败')
        print('---------------------------------------------------')
        # 返回交给下一个管道文件处理
        return item

