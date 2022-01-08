from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")

# def add(request):
    # a = request.GET['a']
    # b = request.GET['b']
    # total = int(a)+int(b)
    # return HttpResponse(str(total))

def add(request, a, b):
    total = int(a)+int(b)
    return HttpResponse(str(total))
