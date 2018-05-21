from django.db import models

# Create your models here.


class Users(models.Model):
    """
    用户表
    """
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32, blank=False)
    email = models.EmailField(blank=False)
    password = models.CharField(max_length=125)
    ip = models.GenericIPAddressField()  # 用户注册时IP
    avatar = models.CharField(max_length=125)  # 用户头像地址
    is_activity = models.IntegerField()  # 用户是否激活
    power = models.CharField(max_length=125)  # 用户权限
    reg_date = models.DateTimeField(auto_now_add=True)  # 用户创建时间
    login_date = models.DateTimeField(auto_now=True)  # 用户上一次登陆时间


class Collect(models.Model):
    """
    收藏表
    """
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField()   # 用户id
    news_id = models.CharField(max_length=20)  # 新闻id


class Logindate(models.Model):
    id = models.AutoField(primary_key=True)
    uid = models.IntegerField()   # 用户id
    ldate = models.DateTimeField(auto_now=True)  # 用户上一次登陆时间


import datetime
class EmailVerifyRecord(models.Model):
    # 验证码
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    # 包含注册验证和找回验证
    send_type = models.CharField(verbose_name=u"验证码类型", max_length=10, choices=(("register",u"注册"), ("forget",u"找回密码")))
    send_time = models.DateTimeField(verbose_name=u"发送时间", default=datetime.datetime)
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)


