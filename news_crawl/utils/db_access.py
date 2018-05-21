from news_crawl.settings import DB
import pymysql


def url_same(url):
    return True
    conn = pymysql.connect(DB['host'], DB['usr'], DB['password'], DB['db_name'], charset='utf8')
    cursor = conn.cursor()
    a = "select count(1) from n_news where title='英伟达称营收增长依赖'"
    b = cursor.fetchone(a)
    print(b)
    conn.close()


if __name__ == '__main__':
    url_same('小法公开对莫拉塔不满：切尔西今年就锋线最烂')
