from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.core.mail import send_mail
from models import Job

# Create your views here.
def home(request):
    t = loader.get_template('home.html')
    c = {'is_home_active': 'active'}
    return HttpResponse(t.render(c))

def case(request):
    t = loader.get_template('case.html')
    c = {'is_case_active': 'active'}
    return HttpResponse(t.render(c))

def about(request):
    if request.POST:
        email = request.POST['Email']
        title = request.POST['Title']
        msg = request.POST['Message']
        # print "%s %s %s" % (email, title, msg)
        send_mail(title, 'from ' + email + msg, 'sitemayerlee@163.com', ['sitemayerlee@163.com'], fail_silently=True)

    t = loader.get_template('about.html')
    joblist = Job.objects.all()
    c = {
        'is_about_active': 'active',
        'joblist': joblist
    }
    return HttpResponse(t.render(c))
