from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.http import Http404
from blog.models import Entry
from django.conf import urls
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.http import require_http_methods
from django.views.decorators.gzip import gzip_page
import datetime
import asyncio
from django.http import QueryDict
from django.template.response import TemplateResponse
import csv
from django.conf import settings
from django.conf import global_settings


class MyTemplateResponse(TemplateResponse):

    def resolve_context(self, context):
        context.update({'foo': 'aaa'})
        return context

def my_render_callback(response):
    print('知道你渲染完了')
    return response

def my_render_callback2(response):
    print('知道你渲染完了222222')
    return None


def index(request):
    # request.session.get('hello')
    # response = HttpResponse('欢迎访问liujiangblog.com\n')
    # response.write('感谢购买视频！')
    # response['Age'] = 120
    # response.content
    # response.status_code = 201
    # response.set_signed_cookie('name','jack')
    # return response
    # return HttpResponse('....')
    # dic = {'name':"jack"}
    # lis = [2,1,2,31]
    # return JsonResponse(lis, safe=False)
    # response = FileResponse(open('media/introduce/jack.txt', 'rb'), as_attachment=True, filename='tom.txt')
    # return response
    # t = MyTemplateResponse(request, 'base_of_app.html', {'foo':'bar'})
    # t. add_post_render_callback(my_render_callback)
    # t. add_post_render_callback(my_render_callback2)
    #
    # return t
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="my.csv"'

    writer = csv.writer(response)
    writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

    return response

def print_request(request):
    for i in [request.scheme, request.body, request.path, request.path_info,
              request.method, request.encoding, request.content_type, request.content_params,
              request.GET, request.POST, request.COOKIES, request.FILES,
              request.META, request.headers, request.resolver_match, request.session,
              request.user
              ]:
        print(i)

    return HttpResponse(status=200)


async def current_datetime(request):
    await asyncio.sleep(2)
    now = datetime.datetime.now()
    html = '<html><body>当前时间：%s</body></html>' % now
    return HttpResponse(html)


def my_view(request):
    foo = []
    if foo:
        return HttpResponse('正常页面')
    else:
        # return HttpResponseNotFound('<h1>您所访问的页面不存在！</h1>')

        # return HttpResponse(status=201)
        return HttpResponse(status=403)


def detail(request):
    # from django.core.exceptions import PermissionDenied
    # if request.user != 'jack':
    #     raise PermissionDenied
    try:
        e = Entry.objects.get(pk=4)
    except Entry.DoesNotExist:
        raise Http404('当前Entry不存在')
    return HttpResponse('文章详细页面')


@requires_csrf_token
def bad_request(request, exception):
    return render(request, '400.html')


@requires_csrf_token
def permission_denied(request, exception):
    pass
    return render(request, '403.html', locals())


@requires_csrf_token
def page_not_found(request, exception):
    return render(request, '404.html')


@requires_csrf_token
def error(request):
    return render(request, '500.html')


from .forms import NameForm, AuthorForm
from django.http import HttpResponseRedirect
from .models import Author
from django.contrib import messages

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            your_name = form.cleaned_data['your_name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            print(your_name, age, email)
            # pass
            return HttpResponseRedirect('/admin/')
        else:
            pass
    else:
        form = NameForm()
    # storage = messages.get_messages(request)
    # for message in storage:
    #     print(message)
    return render(request, 'app/name.html', {'form':form})

def add_author(request):
    if request.method == 'POST':
        f = AuthorForm(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
            # author = Author.objects.create(name=f.cleaned_data.get('name'),
            #                                title=f.cleaned_data.get('title'),
            #                                birth_date=f.cleaned_data.get('birth_date'))
            f.save()
            return HttpResponseRedirect('/admin/')
    else:
        f = AuthorForm()
    return render(request, 'app/add_author.html', {'form':f})


# from django.core.signals import request_finished
# from django.dispatch import receiver


# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print('哈哈，又完成了一个请求，好棒！')
#     print(sender)
#     for i in kwargs:
#         print(i)

# request_finished.connect(my_callback)

import time
import django.dispatch

work_done = django.dispatch.Signal()

def create_signal(request):
    url_path = request.path
    print('我已经完成了工作，现在发送workdone信号给你们，注意接收！')

    work_done.send(create_signal, path=url_path, time=time.time())
    return HttpResponse('200 ok')

import pytz

def set_timezone(request):
    if request.method == 'POST':
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/your_name/')
    else:
        return render(request, 'app/timezone.html', {'timezones': pytz.common_timezones})

from django.contrib.sites.shortcuts import get_current_site

def which_site(request):
    if settings.SITE_ID == 1:
        print('站点1工作正常')
    else:
        print('其它站点也没问题')

    return HttpResponse('当前站点为%s'% get_current_site(request))