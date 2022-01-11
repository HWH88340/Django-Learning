from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context

# Create your views here.
def home(request):
    t = loader.get_template('home.html')
    c = Context({'is_home_active': 'active'})
    return HttpResponse(t.render(c))

def case(request):
    t = loader.get_template('case.html')
    c = Context({'is_case_active': 'active'})
    return HttpResponse(t.render(c))

def about(request):
    t = loader.get_template('about.html')
    c = Context({'is_about_active': 'active'})
    return HttpResponse(t.render(c))
