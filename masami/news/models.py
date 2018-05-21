from django.db import models

# Create your models here.


class News(models.Model):
    """
    新闻表
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=125)
    url = models.TextField()
    summary = models.TextField()  # 摘要
    details = models.TextField()  # 正文
    source = models.CharField(max_length=100)  # 来源
    category = models.CharField(max_length=100)  # 类别
    news_time = models.CharField(max_length=100)  # 时间

    class Meta:
        db_table = "n_news"  # 更改表名


class Comments(models.Model):
    """
    评论表
    """
    id = models.AutoField(primary_key=True)
    nid = models.IntegerField()  # 新闻id
    author = models.CharField(max_length=25)  # 作者
    comments = models.TextField()  # 评论内容
    date = models.DateTimeField(auto_now=True)  # 发表时间

