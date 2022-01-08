from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse

# Create your views here.
def index(request):
    t = loader.get_template('index.html')
    list1 = [3, 5, 9, 8, 4, 6, 10, -1, 45, 6]
    word = 'hello'
    mystring = 'hello django'
    c = Context({
        'list':list1,
        'word':word,
        'str': mystring,
    })
    return HttpResponse(t.render(c))
