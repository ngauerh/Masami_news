from django.conf.urls import url, include
from .views import *


extra_pattern = [
    url(r'^s/', search_news, name='search_news'),
    url(r'^host$', host_news, name='host'),
    url(r'^tech$', tech_news, name='tech'),
    url(r'^soccer$', soccer_news, name='soccer'),
    url(r'^comment$', comment, name='comment'),  # 评论
    url(r'^details/(?P<nid>[0-9]+)$', news_deatils, name='details'),
]


urlpatterns = [
    url(r'^$', show_news, name='show_news'),
    url(r'^n/', include(extra_pattern)),
]


