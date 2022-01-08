from django.shortcuts import render,HttpResponse, HttpResponseRedirect,reverse
from .models import Student,Blog
# Create your views here.
from django.views.generic import TemplateView
from django.template import engines
from django.conf import global_settings

def index(request):
    return HttpResponse('当前的命名空间是%s' % request.resolver_match.namespace)

def detail(request):
    if request.resolver_match.namespace == 'blog_author':
        return HttpResponse('这里是作者的详细页面')
    elif request.resolver_match.namespace == 'blog_publisher':
        return HttpResponse('这里是出版社的详细页面')
    else:
        return HttpResponse('去liujiangblog.com学习Django吧')

def goto(request):
    pass
    return HttpResponseRedirect(reverse('blog:detail', current_app=request.resolver_match.namespace))


# def index(request):
#
#     students = Student.objects.all()
#
#     return render(request, 'blog/index.html', locals())
#
#
# def detail(request, id):
#     student = Student.objects.get(id=id)
#     from django.urls import reverse
#     res = reverse('man', args=(id,))
#     url = student.get_absolute_url()
#     return render(request, 'blog/detail.html', locals())

def man(request, id):
    man = Student.objects.get(id=id)

    return render(request, 'blog/man.html', locals())

def woman(request, id):
    woman = Student.objects.get(id=id)
    return render(request, 'blog/woman.html', locals())


class AboutView(TemplateView):
    template_name = 'about.html'


from django.dispatch import receiver
from app.views import work_done, create_signal



@receiver(work_done, sender=create_signal)
def my_callback(sender, **kwargs):
    print("我在%s时间收到来自%s的信号，请求url为%s" % (kwargs['time'], sender, kwargs["path"]))


from django.core.paginator import Paginator
def paginated_blog(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page = request.GET.get('page')
    # page = int(request.GET.get('page'))
    # if page < 1:
    #     page = 1
    # elif page > paginator.num_pages:
    #     page = paginator.num_pages

    print(paginator.get_page(page))
    current_page = paginator.get_page(page)

    return render(request, 'blog/blog_paginator.html', locals())


from django.core.mail import EmailMessage

email = EmailMessage(
    'Hello',
    'Body goes here',
    'from@example.com',
    ['to1@example.com', 'to2@example.com'],
    ['bcc@example.com'],
    reply_to=['another@example.com'],
    headers={'Message-ID': 'foo'},
)

# email.attach('my_log.png', data, 'image/png')
# email.send()