
from urllib import request, parse
import re
import requests
from lxml import etree
from bs4 import BeautifulSoup


def sina(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content.decode('utf-8'), 'lxml')
    result = html.select('div[class="article"]')
    return str(result)


def sina_s(url):
    base_url = url
    response = requests.get(base_url)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    result = html.xpath('//div[@class ="article"]/p/text()')[0]
    a = result.encode('utf-8')
    print(a.decode('utf-8'))
    return a


def tech163(url):
    response = requests.get(url)
    html = BeautifulSoup(response.content, 'lxml')
    result = html.select('div[class="post_text"]')
    print(result)
    return str(result)



if __name__ == '__main__':
    # sina('http://sports.sina.com.cn/g/laliga/2018-05-10/doc-ihaichqz5924536.shtml')
    # techqq('http://sports.sina.com.cn/g/laliga/2018-05-10/doc-ihaichqz5924536.shtml')
    # sina_s('http://sports.sina.com.cn/g/laliga/2018-05-10/doc-ihaichqz5924536.shtml')
    tech163('http://tech.163.com/18/0509/21/DHD64EN400097U7T.html')