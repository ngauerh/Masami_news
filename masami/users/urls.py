from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^register$', register, name='register'),  # 注册
    url(r'^register_n$', register_n, name='register_n'),
    url(r'^activation$', activation, name='activation'),  # 激活
    url(r'^login$', login, name='login'),   # 登陆
    url(r'^login_n$', login_n, name='login_n'),   # 登陆
    url(r'^logout$', logout, name='logout'),  # 退出
    url(r'^collect$', collect, name='collect'),  # 收藏
    url(r'^p$', personal, name='personal'),  # 个人中心页
    url(r'^verify$', verify, name="verify"),  # 验证码

]
