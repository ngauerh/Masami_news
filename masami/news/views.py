from django.shortcuts import render

# Create your views here.
from news.models import *
from users.models import Collect
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from urllib.parse import urljoin


# 展示
def show_news(request):
    message_list = News.objects.all().order_by('-pk')
    return render(request, 'index.html', {'news_list': message_list})


# 搜索
def search_news(request):
    search_key = request.POST["search"]
    print(search_key)
    if len(search_key.replace(' ', '')) != 0:
        news_list = News.objects.filter(Q(title__icontains=search_key) | Q(summary__icontains=search_key))
        return render(request, 'index.html', {'news_list': news_list})
    else:
        context = {'info': '没有搜索结果！'}
        return render(request, "info.html", context)


# 热门新闻
def host_news(request):
    return render(request, 'index.html')


# 科技新闻
def tech_news(request):
    message_list = News.objects.filter(category='科技').order_by('-pk')
    return render(request, 'index.html', {'news_list': message_list})


# 足球新闻
def soccer_news(request):
    message_list = News.objects.filter(category='足球').order_by('-pk')
    return render(request, 'index.html', {'news_list': message_list})


# 详情
def news_deatils(request, nid):
    ob = News.objects.get(id=nid)
    context = {'ob_list': ob}
    co = Comments.objects.filter(nid=int(nid)).order_by('-pk')
    context['me_list'] = co
    return render(request, 'details.html', context)


# 发表评论
def comment(request):
    try:
        ob = Comments()
        if request.POST["message"].replace(' ', '') != 0:
            ob.comments = request.POST["message"]
            ob.author = request.session["username"]
            ob.nid = request.POST["nid"]
            ob.save()
            # return render(request, 'index.html')
            url = urljoin('/n/details/', request.POST["nid"])
            return redirect(url)
    except:
        url = urljoin('/u/', 'login')
        return redirect(url)


# 收藏
def collect(request):
    ob = Collect()
    ob.news_id = request.POST["nid"]
    ob.uid = request.session["uid"]
    print(ob.news_id)
    ob.save()
    url = urljoin('/n/details/', request.POST["nid"])
    return redirect(url)


