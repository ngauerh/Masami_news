from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import RegisterForm
import time
import hashlib
import random
from django.core.urlresolvers import reverse
from ipware import get_client_ip
from urllib.parse import urljoin
from news.models import News
from utils.send_mail import *

# 注册
def register(request):
    return render(request, "sign_up.html")


def register_n(request):
    try:
        users = Users.objects.all()
        if users.filter(email=request.POST["email"]):
            context = {'info': '邮箱已存在！'}
            return render(request, "info.html", context)
        else:
            ob = Users()
            ob.username = request.POST["username"]
            # 获取密码并md5
            m = hashlib.md5()
            m.update(bytes(request.POST['password'], encoding="utf8"))
            ob.password = m.hexdigest()
            ob.email = request.POST['email']
            ob.is_activity = 0   # 是否激活
            ob.avatar = '/static/avatar/' + str(random.randint(0, 10)) + '.jpg'
            ob.power = 0  # 权限

            client_ip, is_routable = get_client_ip(request)
            if client_ip is None:
                ob.ip = '0'
            else:
                # We got the client's IP address
                if is_routable:
                    ob.ip = client_ip
                    # The client's IP address is publicly routable on the Internet
                else:
                    ob.ip = client_ip
                # The client's IP address is private

            ob.save()
            context = {'info': '注册成功！'}
            # send_email(request.POST["email"], "register")
            return render(request, "info.html", context)
    except:
        context = {'info': '添加失败！'}
        return render(request, "info.html", context)


# 激活
def activation(request):
    pass


# 登陆
def login(request):
    return render(request, "sign_in.html")


def login_n(request):
    # 校验验证码
    verifycode = request.session['verifycode']
    code = request.POST['code'].lower()
    if verifycode != code:
        context = {'info': '验证码错误！'}
        return render(request, "info.html", context)
    try:
        user = Users.objects.get(email=request.POST['email'])
        # 根据账号获取登陆着信息
        m = hashlib.md5()
        m.update(bytes(request.POST['password'], encoding="utf-8"))
        if user.password == m.hexdigest():
            # 若此处登陆成功，将 当前登陆信息放到session中，并跳转页面
            request.session['username'] = user.username
            request.session['uid'] = user.id
            try:
                ld = Logindate.objects.get(id=user.id)
                ld.ldate = time.time()
                ld.save()
            except:
                ob = Logindate()
                ob.uid = user.id
                ob.save()

            return redirect(reverse('show_news'))
        else:
            context = {'info': '登陆密码出错！'}
            return render(request, 'sign_in.html', context)
    except:
        context = {'info': '账号不存在！'}
        return render(request, 'info.html', context)


# 退出
def logout(request):
    ld = Users.objects.get(id=request.session['uid'])
    ld.login_date = Logindate.objects.get(id=request.session['uid'])
    ld.save()
    del request.session['username']
    del request.session['uid']
    return redirect(reverse('show_news'))


# 个人主页
def personal(request):
    user = Users.objects.get(id=request.session['uid'])
    message_list = {'message_list': user}
    collect_list = Collect.objects.filter(uid=request.session['uid'])
    news_list = []
    for i in collect_list:
        news = News.objects.get(id=i.news_id)
        news_list.append(news)
    message_list["collect"] = news_list
    return render(request, "personal.html", message_list)


# 个人收藏
def collect(request):
    ob = Collect()
    ob.news_id = request.POST["nid"]
    ob.uid = request.session["uid"]
    ob.save()
    url = urljoin('/n/details/', request.POST["nid"])
    return redirect(url)


# 验证码
def verify(request):
    # 引入绘图模块
    from PIL import Image, ImageDraw, ImageFont
    # 引入随机函数模块
    import random
    # 定义变量，用于画面的背景色、宽、高
    # bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    bgcolor = (150, 154, 194)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点

    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)

    # 定义验证码的备选值
    # str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    str1 = 'ABCDEFGHIJasdfghjk'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象
    font = ImageFont.truetype('static/fonts/STXIHEI.TTF', 23)
    # font = ImageFont.load_default().font
    for i in range(0, 4):
        # 构造字体颜色
        fontcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        # 绘制4个字
        draw.text((5 + i * 24, -4), rand_str[i], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步验证
    request.session['verifycode'] = rand_str.lower()
    # 内存文件操作
    import io
    buf = io.BytesIO()
    # 将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')






